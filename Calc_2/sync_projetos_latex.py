#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sync_projetos_latex.py

Atualiza o repositório GitHub do guarda-chuva Projetos_Latex:
- (opcional) copia novos projetos de C:\LaTex_Projects\* para dentro de C:\LaTex_Projects\Projetos_Latex\*
- git pull (rebase)
- git add -A
- commit (se houver mudanças)
- git push

Uso:
  python sync_projetos_latex.py
  python sync_projetos_latex.py --sync-sources
  python sync_projetos_latex.py --sync-sources --message "Atualiza projetos"
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


DEFAULT_SOURCE_ROOT = Path(r"C:\LaTex_Projects")
DEFAULT_REPO_ROOT = Path(r"C:\LaTex_Projects\Projetos_Latex")


def run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    """Run a git command and return CompletedProcess. Raises on non-zero."""
    cmd = ["git"] + args
    p = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        shell=False,
    )
    if p.returncode != 0:
        raise RuntimeError(
            f"Falha executando: {' '.join(cmd)}\n"
            f"cwd: {cwd}\n"
            f"stdout:\n{p.stdout}\n"
            f"stderr:\n{p.stderr}\n"
        )
    return p


def is_git_repo(path: Path) -> bool:
    return (path / ".git").exists() and (path / ".git").is_dir()


def should_skip_source_dir(d: Path, repo_root: Path) -> bool:
    # pule o próprio repo e pastas ocultas / temporárias comuns
    if d.resolve() == repo_root.resolve():
        return True
    name = d.name.lower()
    if name in {".git", ".vs", ".vscode", "__pycache__"}:
        return True
    # opcional: pule pastas que começam com '_' se você usa como junkyard/backups
    # if d.name.startswith("_"):
    #     return True
    return False


def safe_copy_tree(src: Path, dst: Path) -> None:
    """
    Copia src/* para dst/ (criando dst).
    - Se arquivo existe em dst, sobrescreve.
    - Mantém metadados básicos.
    """
    dst.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(src):
        root_p = Path(root)
        rel = root_p.relative_to(src)
        target_root = dst / rel
        target_root.mkdir(parents=True, exist_ok=True)

        # não copiar .git de projetos que por acaso tenham
        dirs[:] = [d for d in dirs if d.lower() != ".git"]

        for fn in files:
            src_file = root_p / fn
            target_file = target_root / fn
            # cria pasta pai e copia
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, target_file)


def sync_sources_into_repo(source_root: Path, repo_root: Path) -> list[str]:
    """
    Copia cada pasta de projeto em source_root para dentro do repo_root,
    criando/atualizando subpastas equivalentes.

    Retorna lista de projetos sincronizados.
    """
    synced: list[str] = []

    if not source_root.exists():
        raise FileNotFoundError(f"source_root não existe: {source_root}")
    if not repo_root.exists():
        raise FileNotFoundError(f"repo_root não existe: {repo_root}")

    for d in source_root.iterdir():
        if not d.is_dir():
            continue
        if should_skip_source_dir(d, repo_root):
            continue

        # regra: só sincroniza pastas "de projeto" (heurística simples)
        # Ex.: se tem pelo menos um .tex em qualquer nível OU arquivos típicos
        has_tex = any(d.rglob("*.tex"))
        if not has_tex:
            # Se você quiser sincronizar tudo mesmo sem .tex, remova este if
            continue

        dst = repo_root / d.name
        safe_copy_tree(d, dst)
        synced.append(d.name)

    return synced


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=str, default=str(DEFAULT_REPO_ROOT), help="Pasta do repo Projetos_Latex")
    ap.add_argument("--source-root", type=str, default=str(DEFAULT_SOURCE_ROOT), help="Pasta mãe dos projetos (LaTex_Projects)")
    ap.add_argument("--sync-sources", action="store_true", help="Copia novos/atualiza projetos do source-root para dentro do repo")
    ap.add_argument("--message", type=str, default="", help="Mensagem de commit (opcional)")
    args = ap.parse_args()

    repo_root = Path(args.repo)
    source_root = Path(args.source_root)

    if not is_git_repo(repo_root):
        print(f"ERRO: {repo_root} não parece um repositório Git (faltou .git).", file=sys.stderr)
        return 2

    # 1) opcional: copiar projetos para dentro do repo
    synced = []
    if args.sync_sources:
        synced = sync_sources_into_repo(source_root, repo_root)
        if synced:
            print("Projetos sincronizados para o repo:", ", ".join(synced))
        else:
            print("Nenhum projeto novo com .tex encontrado para sincronizar (ou nada a copiar).")

    # 2) pull (rebase)
    print("git pull --rebase ...")
    run_git(["pull", "--rebase"], cwd=repo_root)

    # 3) add tudo (inclui novos projetos/pastas já presentes no repo)
    print("git add -A ...")
    run_git(["add", "-A"], cwd=repo_root)

    # 4) checar se tem mudanças staged
    status = run_git(["status", "--porcelain"], cwd=repo_root).stdout.strip()
    if not status:
        print("Nada para commitar (working tree clean).")
        return 0

    # 5) commit e push
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    if args.message.strip():
        msg = args.message.strip()
    else:
        msg = f"Sync Projetos_Latex ({ts})"
        if synced:
            msg += f" +{len(synced)} projetos"

    print(f"git commit -m \"{msg}\" ...")
    run_git(["commit", "-m", msg], cwd=repo_root)

    print("git push ...")
    run_git(["push"], cwd=repo_root)

    print("OK: atualizado no GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
