### Run the app in local environment

```sh
docker compose -f ./docker/docker-compose.yaml -p parkingspots up
```

### Ruff as Pre-commit Hook

Ruff is configured as a pre-commit hook.  
To set it up, run the following commands in order:

**Install pre-commit:**
```bash
pip install pre-commit
```

**Install the hook:**
```bash
pre-commit install
```