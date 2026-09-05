# 🔐 Lab 001: SHA-256 File Integrity Verification

## 🎯 Objective

Demonstrate how SHA-256 hashing can be used to verify file integrity and detect when a file has been modified.

This lab demonstrates the **Integrity** component of the CIA Triad.

---

## 🛠️ Tools Used

- Windows
- Windows PowerShell
- SHA-256
- PowerShell `Get-FileHash` command
- Notepad

---

## 🧪 Lab Procedure

### Step 1 — Create the Original File

I created a text file named `important-file.txt` containing:

> This is the original Security+ lab file.

### Step 2 — Calculate the Original SHA-256 Hash

I used PowerShell to calculate the SHA-256 hash of the original file:

```powershell
Get-FileHash C:\Users\jesse\OneDrive\Desktop\Security-Lab-001\important-file.txt
```

Original SHA-256:

```text
BF0194F4FCB92041FE7509CA0B618B1A9C329ED36361425E61D976DECE4D7315
```

### Step 3 — Modify the File

I modified `important-file.txt` by adding the following line:

> This file has now been modified.

This changed the contents of the file while keeping the same file name.

### Step 4 — Calculate the SHA-256 Hash Again

After modifying the file, I ran the same PowerShell command again:

```powershell
Get-FileHash C:\Users\jesse\OneDrive\Desktop\Security-Lab-001\important-file.txt
```

New SHA-256:

```text
2F601D026E8C859F879DD48E5520193A8A34CCD1430047C7353697A9E79C6E6D
```

---

## 🔎 Results

The original and modified SHA-256 hashes were different.

**Original:**
```text
BF0194F4FCB92041FE7509CA0B618B1A9C329ED36361425E61D976DECE4D7315
```

**Modified:**
```text
2F601D026E8C859F879DD48E5520193A8A34CCD1430047C7353697A9E79C6E6D
```

Because the hashes no longer match, I can determine that the contents of the file changed.

SHA-256 does not tell me what changed inside the file. Instead, the hash comparison provides a way to verify whether the file is still identical to the original.

---

## 🔐 Security Concepts Demonstrated

- CIA Triad — Integrity
- Cryptographic hashing
- SHA-256
- File integrity verification
- Detection of file modification

---

## 📚 What I Learned

This lab demonstrated the difference between hashing and encryption.

Encryption is primarily used to protect **confidentiality**, while hashing can be used to verify **integrity**.

By calculating a SHA-256 hash before and after modifying a file, I observed that changing the file contents produced a completely different hash.























