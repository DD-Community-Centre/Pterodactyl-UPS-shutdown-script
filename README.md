# Pterodactyl-UPS-shutdown-script

## Requirements:

- CyberPower UPS and its CLI tool `pwrstat`
- Python 3
- PyPI package `py-dactyl`: https://pypi.org/project/py-dactyl/

## Environment Variables

- `PTERODACTYL_API_URL`: Pterodactyl API URL
- `PTERODACTYL_CLIENT_KEY`: Pterodactyl Client API key
- `PTERODACTYL_APP_KEY`: Pterodactyl Application API key

## Usage

- Run `pip install -r requirements.txt`
- You should find the UPS shutdown/lower battery scripts under `/etc`:
```
/etc/pwrstatd-lowbatt.sh
/etc/pwrstatd-powerfail.sh
```
- Append the following lines to the UPS shutdown/low battery scripts:
```
export PTERODACTYL_API_URL="PTERODACTYL_API_URL"
export PTERODACTYL_CLIENT_KEY="PTERODACTYL_CLIENT_KEY"
export PTERODACTYL_APP_KEY="PTERODACTYL_APP_KEY"
PYTHON3_BIN=$(which "python3")
SHUTDOWN_SCRIPT='your UPS shutdown script path'
"$PYTHON3_BIN" "$SHUTDOWN_SCRIPT"
```
- Run the following scripts:
```
pwrstat -pwrfail -delay 60 -active on -cmd /etc/pwrstatd-powerfail.sh -duration 60 -shutdown on 
pwrstat -lowbatt -delay 5 -active on -cmd /etc/pwrstatd-lowbatt.sh -duration 60 -shutdown on 
```