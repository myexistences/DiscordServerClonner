# 🔁 Discord Server Clonner — Advanced Server Cloner & Asset Backup Utility

[![GitHub Views](https://komarev.com/ghpvc/?username=myexistences&repo=DiscordServerClonner&color=blueviolet&style=flat&label=Views)](https://github.com/myexistences/DiscordServerClonner)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/myexistences/DiscordServerClonner?style=social)](https://github.com/myexistences/DiscordServerClonner/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/myexistences/DiscordServerClonner?style=social)](https://github.com/myexistences/DiscordServerClonner/network/members)

A powerful and user-friendly Discord utility for duplicating servers, downloading stickers/emojis, retrieving guild information, and verifying token access — all **without needing administrator privileges** on the target server.

> ⚙️ **Developed by** [@myexistences](https://github.com/myexistences)  
> 🚫 **No Admin Rights Required** | 🎒 **Backup-Friendly** | 🧩 **Modular Design**

---

## 📌 Key Features

- ✅ **Complete Server Cloning** — Duplicate entire server configurations
- 🧸 **Asset Export** — Download custom stickers and emojis in bulk
- 📊 **Guild Intelligence** — Fetch comprehensive server information
- 🔑 **Token Validation** — Verify token validity and permissions
- 🧩 **Modular Architecture** — Clean, maintainable, and extensible codebase
- 🔐 **Built-in Attribution Protection** — Respects original author credits
- ⛔ **Permission-Free Operation** — Works without admin privileges

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Valid Discord user/bot token
- Basic command line knowledge

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/myexistences/DiscordServerClonner.git
   cd DiscordServerClonner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your token**
   ```bash
   echo "YOUR_DISCORD_TOKEN_HERE" > token.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```
DiscordServerClonner/
├── 📄 main.py                    # Main application entry point
├── 📄 token.txt                  # Discord token storage (user-provided)
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # This file
├── 📁 func/                      # Core functionality modules
│   ├── 🔧 cloner.py             # Server cloning logic
│   ├── 🔧 clone_Copier.py       # Channel/role duplication
│   ├── 🔧 clone_emojis.py       # Emoji extraction and download
│   ├── 🔧 clone_stickers.py     # Sticker backup utility
│   ├── 🔧 guild_info.py         # Server information retrieval
│   └── 🔧 token_checker.py      # Token validation service
├── 📁 utils/                     # Utility functions
│   └── 🔧 innit.py              # Core utilities and attribution
└── 📁 downloads/                 # Downloaded assets (auto-created)
```

---

## 🖥️ Usage Guide

### Interactive Menu

Launch the application to access the interactive menu:

```
╔══════════════════════════════════════╗
║     Discord Server Clonner v2.0     ║
║    Advanced Server Management        ║
╠══════════════════════════════════════╣
║ [01] Clone Server                    ║
║ [02] Clone Stickers                  ║
║ [03] Clone Emojis                    ║
║ [04] Server Info                     ║
║ [05] Token Checker                   ║
║ [00] Exit                            ║
╚══════════════════════════════════════╝
```

### Command Examples

1. **Server Cloning**
   - Select option `[01]`
   - Enter target Guild ID
   - Wait for completion confirmation

2. **Asset Backup**
   - Choose `[02]` for stickers or `[03]` for emojis
   - Provide Guild ID
   - Assets saved to `./downloads/` folder

3. **Server Analysis**
   - Select `[04]` to get detailed server information
   - View member count, channels, roles, and more

---

## 🔧 Configuration

### Token Setup

Place your Discord token in `token.txt`:

```
YOUR_DISCORD_TOKEN_HERE
```

⚠️ **Security Notice**: Keep your token private and never commit it to version control.

### Environment Variables (Optional)

```bash
export DISCORD_TOKEN="your_token_here"
export OUTPUT_DIR="./custom_downloads"
export LOG_LEVEL="INFO"
```

---

## 💡 Use Cases

| Scenario | Benefit |
|----------|---------|
| 🧰 **Server Backup** | Create complete backups of your Discord servers |
| 🧪 **Testing Environment** | Set up staging servers for bot development |
| 🔍 **Server Analysis** | Analyze server structure and member data |
| ✅ **Token Validation** | Verify token permissions and validity |
| 🗃️ **Asset Management** | Bulk download and organize server assets |
| 📊 **Audit & Compliance** | Document server configurations for compliance |

---

## 🔐 Security & Privacy

- **Token Safety**: Your token never leaves your local machine
- **No Data Storage**: No user data is permanently stored
- **Attribution Protection**: Built-in checks prevent unauthorized modifications
- **Permission Minimal**: Operates with minimal Discord permissions

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings for new functions
- Include error handling
- Maintain attribution headers
- Test thoroughly before submitting

---

## 📋 Requirements

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.9 or higher
- **Memory**: 256MB RAM minimum
- **Storage**: 50MB available space

### Python Dependencies
```txt
requests>=2.31.0
pystyle>=2.4.0
colorama>=0.4.6
python-dotenv>=1.0.0
```

---

## 🚨 Disclaimer

⚠️ **Important Legal Notice**

- This tool is provided for **educational**, **testing**, and **legitimate backup** purposes only
- Using Discord user tokens may violate Discord's Terms of Service
- The developer assumes **no responsibility** for misuse or policy violations
- Users are responsible for ensuring compliance with Discord's guidelines
- **Use at your own risk**

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 @myexistences

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 🙏 Attribution

**Created by**: [@myexistences](https://github.com/myexistences)

```python
# This software was created by @myexistences
# GitHub: https://github.com/myexistences
# Please respect the author's work and retain all credits
```

> **Note**: Removing or modifying attribution headers is prohibited and may violate license terms.

---

## 📞 Support & Contact

- 🐛 **Bug Reports**: [Open an Issue](https://github.com/myexistences/DiscordServerClonner/issues)
- 💡 **Feature Requests**: [Discussion Board](https://github.com/myexistences/DiscordServerClonner/discussions)
- 📧 **Direct Contact**: [Email](mailto:mdrabbanymc130@gmail.com)
- 💬 **Community**: [Discord Server](https://discord.gg/K8CZkkCDr3)

---

## 🎯 Roadmap

- [ ] **v2.1**: GUI interface with Tkinter/PyQt
- [ ] **v2.2**: Batch processing for multiple servers
- [ ] **v2.3**: Advanced filtering and search options
- [ ] **v2.4**: Cloud backup integration
- [ ] **v3.0**: Web dashboard with real-time monitoring

---

## ⭐ Show Your Support

If this project helped you, please consider:

- ⭐ **Starring** this repository
- 🍴 **Forking** for your own modifications
- 📢 **Sharing** with the community

---

<div align="center">

**Made with ❤️ by [@myexistences](https://github.com/myexistences)**

[![GitHub](https://img.shields.io/badge/GitHub-myexistences-black?style=for-the-badge&logo=github)](https://github.com/myexistences)

*Thank you for using DiscordSync! 🚀*

</div>
