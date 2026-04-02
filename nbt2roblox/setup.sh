cat << 'EOF' > setup.sh
#!/bin/bash
echo "🚀 Starting environment setup..."
sudo apt update
sudo apt install -y python3-venv python3-pip
if [ -d "venv" ]; then
    rm -rf venv
fi
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install nbtlib
deactivate
echo "✅ Setup complete! Use ./run.sh your_file.nbt to convert."
EOF
chmod +x setup.sh
