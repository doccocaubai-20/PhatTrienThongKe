@echo off
title GaraMan - Chạy Kiểm Thử Đơn Vị (JUnit Test)
chcp 65001 > nul
echo ================================================================
echo   ĐANG CHẠY TOÀN BỘ 21 UNIT TEST (KIỂM THỬ ĐƠN VỊ DAO) - GARAMAN
echo ================================================================
mvn test
pause
