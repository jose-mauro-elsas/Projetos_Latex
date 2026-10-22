@echo off
copernicusmarine subset ^
  --dataset-id "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m" ^
  --variable "thetao" ^
  --minimum-longitude -54.0 ^
  --maximum-longitude -38.0 ^
  --minimum-latitude -30.0 ^
  --maximum-latitude -17.0 ^
  --minimum-depth 0.0 ^
  --maximum-depth 1.0 ^
  --start-datetime "2025-01-01T00:00:00" ^
  --end-datetime "2025-12-31T23:59:59" ^
  --output-filename "D:\LaTex_Projects\Cartografia\SIG_BRASIL\06_OCEANOGRAFIA\Copernicus\temperatura_superficial_2025.nc"
pause
