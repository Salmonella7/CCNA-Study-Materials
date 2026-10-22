---
title: InSighter Hub
aliases:
  - InSighter
tags:
  - insighter
  - project
type: hub
---

# InSighter Hub

> [!abstract] AI-assisted insider threat detection
> Local Flask + PyQt6 proof of concept. Isolation Forest + One-Class SVM ensemble, RBAC (admin / compliance / management), encrypted event storage.

## Layers

- [[Core and Backend|Core & Backend]]
- [[Security, Privacy and Auth|Security, Privacy & Auth]]
- [[LLM Advisor|LLM Advisor]]
- [[CERT Dataset and Baselines|CERT Dataset & Baselines]]
- [[Desktop App PyQt6|Desktop App (PyQt6)]]
- [[Tests|Tests]]
- [[Web Templates|Web Templates]]
- [[LLM Benchmarks|LLM Benchmarks]]
- [[Ops and Config|Ops & Config]]

## Entry points

- [[InSighter/notes/app|app.py]] — Flask app and HTTP routes
- [[InSighter/notes/desktop_app/main|desktop_app/main.py]] — PyQt6 launcher
- [[InSighter/notes/llm_advisor|llm_advisor.py]] — local LLM risk explanations
- [[InSighter/notes/model|model.py]] — detection + scoring pipeline
- [[InSighter/source/README|README]] — project README (original)
- [[InSighter/notes/How to run the current system|How to run the current system]] — run notes (original)

## How the graph is wired

Each note is a source file. Edges come from real Python imports, Jinja template `extends`/`include`, and the test → module mapping, so the graph view shows the actual dependency structure of the project.

## Groups

- [[Core and Backend|Core & Backend]]
- [[Security, Privacy and Auth|Security, Privacy & Auth]]
- [[LLM Advisor|LLM Advisor]]
- [[CERT Dataset and Baselines|CERT Dataset & Baselines]]
- [[Desktop App PyQt6|Desktop App (PyQt6)]]
- [[Tests|Tests]]
- [[Web Templates|Web Templates]]
- [[LLM Benchmarks|LLM Benchmarks]]
- [[Ops and Config|Ops & Config]]

## Related vault notes

- [[Cyber Security Talk (4-22-25)]] — portfolio context for this project

---

Source project: `D:\Capstoners\InSighter` (clone of `Jayyydrian/InSighter`)
