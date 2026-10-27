with open('1.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

insert_idx = -1
for i in range(10212, len(lines)):
    if "def _sec(" in lines[i]:
        insert_idx = i
        break

if insert_idx != -1:
    lines.insert(insert_idx, """
    def _on_lang_changed(self, idx):
        lang_code = self.lang_cb.itemData(idx)
        SETTINGS["language"] = lang_code
        save_settings()
        QMessageBox.information(self, T("Khởi động lại"), T("Vui lòng khởi động lại ứng dụng để áp dụng ngôn ngữ mới."))
""")

with open('1.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
