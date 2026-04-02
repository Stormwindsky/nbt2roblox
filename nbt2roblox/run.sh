cat << 'EOF' > run.sh
#!/bin/bash
if [ ! -d "venv" ]; then
    echo "❌ Error: 'venv' directory not found. Run ./setup.sh first."
    exit 1
fi
source venv/bin/activate
if [ -z "$1" ]; then
    echo "Usage: ./run.sh filename.nbt"
else
    python nbt2roblox.py "$1"
fi
deactivate
EOF
chmod +x run.sh
