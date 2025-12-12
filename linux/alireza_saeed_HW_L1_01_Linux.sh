#!/bin/bash

clear

# Color Definition
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
BOLD="\e[1m"
RESET="\e[0m"

# print banner for title ant author
echo -e "${BOLD}${YELLOW}"
cat << "EOF"
--- gol baray gol ---

   /\_/\
  ( o.o ) づ  @-->--
   > ^ <

--- sorry for delay(: ---
HW_L1_01_Linux
by: alireza saeed
EOF
echo -e "${RESET}"

sleep 1 # pause for 1 second

# functions for print colored text

section() {
  echo -e "${BOLD}${MAGENTA}\n[ $1 ]${RESET}"
}

info() {
  echo -e "${GREEN}--> $1${RESET}"
}

warn() {
  echo -e "${YELLOW}[i] $1${RESET}"
}

# ===============================
section "1) Environment Preparation"


AUDIT_DIR=~/exam_results/audit
info "Creating audit directory at: $AUDIT_DIR"
mkdir -p "$AUDIT_DIR"

# notes.txt
info "Creating txt.notes file (with heading comment)"
echo "# Notes for system audit " > "$AUDIT_DIR/notes.txt"

# cwd.txt
info "Saving current working directory to cwd.txt"
echo "# Current working directory cwd.txt" > "$AUDIT_DIR/cwd.txt"
pwd >> "$AUDIT_DIR/cwd.txt"

# ===============================
section "2) User Account Analysis (from /etc/passwd)"


# users.txt
info "Extracting all usernames to txt.users"
echo "# All system usernames users.txt" > "$AUDIT_DIR/users.txt"
cut -d: -f2 /etc/passwd >> "$AUDIT_DIR/users.txt"

# users_bash
info "Finding users with /bin/bash shell to users_bash.txt"
echo "# Users with /bin/bash login shell users_bash.txt" > "$AUDIT_DIR/users_bash.txt"
awk -F: -v shell="/bin/bash" '$7=="shell"{print $1}' /etc/passwd >> "$AUDIT_DIR/users_bash.txt"

# preview_shell
info "Preview: replace /bin/bash with /usr/bin/zsh (first 5 lines only) -> preview_shell.txt"
echo "# Preview of passwd with bash -> zsh preview_shell.txt" > "$AUDIT_DIR/preview_shell.txt"
sed 's#/bin/bash#/usr/bin/zsh#g' /etc/passwd | head -n 5 >> "$AUDIT_DIR/preview_shell.txt"

# ===============================
section "3) System Information"


info "Saving kernel name and version (uname)"
echo "# System info (kernel name & version)" > "$AUDIT_DIR/sysinfo.txt"
echo "uname -srm:" >> "$AUDIT_DIR/sysinfo.txt"
uname -srm >> "$AUDIT_DIR/sysinfo.txt"

info "Appending architecture (arch) to sysinfo.txt"
echo "Architecture (arch):" >> "$AUDIT_DIR/sysinfo.txt"
arch >> "$AUDIT_DIR/sysinfo.txt"

# summary_group.txt
info "Saving first 3 and last 2 lines of /etc/group"
echo "# Summary of /etc/group (first 3 & last 2 lines)" > "$AUDIT_DIR/summary_group.txt"
head -n 3 /etc/group >> "$AUDIT_DIR/summary_group.txt"
tail -n 2 /etc/group >> "$AUDIT_DIR/summary_group.txt"

# ===============================
section "4) Config & Log Files"


# files_conf.txt
info "Listing all *.conf files under /etc"
echo "# List of .conf files under /etc" > "$AUDIT_DIR/files_conf.txt"
# 2>/dev/null its mute error for clean output
find /etc -type f -name "*.conf" 2>/dev/null >> "$AUDIT_DIR/files_conf.txt"

# logs_top.txt
info "Finding top 10 largest log files under /var/log"
echo "# Top 10 largest log files in /var/log" > "$AUDIT_DIR/logs_top.txt"
find /var/log -type f -exec du -h {} + 2>/dev/null | sort -hr | head -n 10 >> "$AUDIT_DIR/logs_top.txt"

# ===============================
section "5) Permission Management"

warn "Copying /etc/hosts to audit directory as hosts.bak"
cp /etc/hosts "$AUDIT_DIR/hosts.bak"

warn "Setting permissions so only owner can read & write (chmod 600)"
chmod 600 "$AUDIT_DIR/hosts.bak"

info "Saving ls -l output of hosts.bak to hosts_perm.txt"
echo "# Permission of hosts.bak (hosts_perm.txt)" > "$AUDIT_DIR/hosts_perm.txt"
ls -l "$AUDIT_DIR/hosts.bak" >> "$AUDIT_DIR/hosts_perm.txt"

# ===============================
section "6) Cleanup"

info "Deleting all .txt files in audit dir except hosts_perm.txt and notes.txt"
find "$AUDIT_DIR" -type f -name "*.txt" ! -name "hosts_perm.txt" -name "notes.txt" -delete 2>/dev/null

echo -e "${BOLD}${BLUE}\nSystem audit completed successfully.${RESET}"
echo -e "${CYAN}All results are in: $AUDIT_DIR${RESET}"
echo -e "${BOLD}${YELLOW} step 6 dont working because i forget to add '!' for see results, Have a nice day!${RESET}"
