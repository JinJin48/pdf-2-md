# Run the PDF to Markdown converter in background mode
# This launches python in a separate process that persists even if this terminal is closed.

$scriptPath = Join-Path $PSScriptRoot "pdf-converter-4-dify.py"

# Check if python is available
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found in PATH."
    exit 1
}

Write-Host "Starting PDF to Markdown Converter in background..."
Write-Host "Logs will be written to 'conversion.log'"

# Start process detached
# -WindowStyle Hidden: Hides the window
# -PassThru: Returns the process object
$process = Start-Process -FilePath "python" -ArgumentList "`"$scriptPath`" --background" -WindowStyle Hidden -PassThru

Write-Host "Process started with ID: $($process.Id)"
Write-Host "You can close this window now."
