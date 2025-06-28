#!/bin/bash
echo "Testing environment..."
docker compose exec api python -c "import os; print(f'REPLICATE_API_TOKEN exists: {bool(os.getenv(\"REPLICATE_API_TOKEN\"))}')"