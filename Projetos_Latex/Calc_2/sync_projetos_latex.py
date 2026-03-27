@'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_ROOT = Path(r"C:\LaTex_Projects")
DEFAULT_REPO_ROOT   = Path(r"C:\LaTex_Projects\Projetos_Latex")

DEFAULT_WHITELIST = ["Calc_2", "Estatistica", "Descomissionamento", "Geometria"]

SKIP_DIRS_ALWAYS = {".git", ".vs", "__pycache__", ".vscode"}  # ajuste se quiser versionar .vscode

def run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    cmd = ["git"] + args
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(
            f"Falha executando: {' '.join(cmd)}\n"
            f"cwd: {cwd}\n"
            f"stdout:\n{p.stdout}\n"
            f"stderr:\n{p.stderr}\n"
        )
    return p

def is_git_repo(path: Path) -> bool:
    return (path / ".git").is_dir()

def safe_copy_tree(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(src):
        root_p = Path(root)
        rel = root_p.relative_to(src)
        target_root = dst / rel
        target_root.mkdir(parents=True, exist_ok=True)

        # não copiar diretórios indesejados
        dirs[:] = [d for d in dirs if d.lower() not in {x.lower() for x in SKIP_DIRS_ALWAYS}]

        for fn in files:
            # exemplo: ignorar backups comuns (ajuste se quiser)
            if fn.lower().endswith((".bak", ".tmp")):
                continue
            src_file = root_p / fn
            target_file = target_root / fn
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, target_file)

def sync_selected_projects(source_root: Path, repo_root: Path, whitelist: list[str]) -> list[str]:
    synced: list[str] = []
    for name in whitelist:
        src = source_root / name
        if not src.is_dir():
            continue
        # só sincroniza se tiver pelo menos um .tex em algum nível
        if not any(src.rglob("*.tex")):
            continue
        safe_copy_tree(src, repo_root / name)
        synced.append(name)
    return synced

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(DEFAULT_REPO_ROOT))
    ap.add_argument("--source-root", default=str(DEFAULT_SOURCE_ROOT))
    ap.add_argument("--sync-sources", action="store_true")
    ap.add_argument("--only", default=",".join(DEFAULT_WHITELIST),
                   help="Lista (separada por vírgula) de pastas para sincronizar, ex: Calc_2,Geometria")
    ap.add_argument("--message", default="")
    ap.add_argument("--no-pull", action="store_true", help="Não executar git pull --rebase")
    args = ap.parse_args()

    repo_root = Path(args.repo)
    source_root = Path(args.source_root)

    if not is_git_repo(repo_root):
        print(f"ERRO: {repo_root} não parece um repositório Git (.git não encontrado).", file=sys.stderr)
        return 2

    # 1) Atualiza repo antes de mexer nos arquivos
    if not args.no_pull:
        print("git pull --rebase ...")
        run_git(["pull", "--rebase"], cwd=repo_root)

    # 2) Copia projetos selecionados
    synced = []
    if args.sync_sources:
        whitelist = [x.strip() for x in args.only.split(",") if x.strip()]
        synced = sync_selected_projects(source_root, repo_root, whitelist)
        if synced:
            print("Projetos sincronizados:", ", ".join(synced))
        else:
            print("Nenhum projeto sincronizado (não encontrado ou sem .tex).")

    # 3) Add/commit/push
    print("git add -A ...")
    run_git(["add", "-A"], cwd=repo_root)

    status = run_git(["status", "--porcelain"], cwd=repo_root).stdout.strip()
    if not status:
        print("Nada para commitar (working tree clean).")
        return 0

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = args.message.strip() or f"Sync Projetos_Latex ({ts})" + (f" [{','.join(synced)}]" if synced else "")
    print(f'git commit -m "{msg}" ...')
    run_git(["commit", "-m", msg], cwd=repo_root)

    print("git push ...")
    run_git(["push"], cwd=repo_root)

    print("OK: atualizado no GitHub.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'@ | Set-Content -Encoding utf8 C:\LaTex_Projects\sync_projetos_latex.py
