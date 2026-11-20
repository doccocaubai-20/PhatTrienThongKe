<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<style>
    * { box-sizing: border-box; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        margin: 0; padding: 20px;
        background-color: #f1f5f9; color: #1e293b;
    }
    .header-bar {
        background: #1e293b; color: white;
        padding: 14px 24px; border-radius: 8px;
        margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header-bar h2 { margin: 0; font-size: 20px; }
    .container {
        background: #ffffff; padding: 24px; border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        max-width: 1050px; margin: 0 auto;
    }
    h3 { margin-top: 0; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
    table.data-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    table.data-table th, table.data-table td { border: 1px solid #cbd5e1; padding: 10px 12px; text-align: left; }
    table.data-table th { background-color: #f8fafc; font-weight: 600; color: #334155; }
    .info-box { background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 16px; border-radius: 6px; margin-bottom: 16px; }
    .form-control { padding: 8px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px; }
    .btn {
        display: inline-block; padding: 8px 16px; font-size: 14px; font-weight: 500;
        border-radius: 6px; border: none; cursor: pointer; text-decoration: none;
        background-color: #2563eb; color: white;
    }
    .btn:hover { opacity: 0.9; }
    .btn-primary { background-color: #2563eb; color: white; }
    .btn-secondary { background-color: #64748b; color: white; }
    .btn-success { background-color: #16a34a; color: white; }
</style>

<div class="header-bar">
    <h2>GaraMan - Quản Lý Gara Ô Tô</h2>
</div>
