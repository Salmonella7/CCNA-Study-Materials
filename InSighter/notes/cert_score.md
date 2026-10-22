---
title: cert_score.py
aliases:
  - cert_score.py
tags:
  - insighter
  - insighter/cert
type: source-module
module: cert_score.py
path: InSighter/source/cert_score.py
category: CERT Dataset & Baselines
project: InSighter
---

# cert_score.py

> [!info] CERT Dataset & Baselines
> Source: `InSighter/source/cert_score.py`
> InSighter project file — see [[InSighter Hub|the hub]] and [[CERT Dataset and Baselines|CERT Dataset & Baselines]].

## Purpose

Part of the **CERT Dataset & Baselines** layer of InSighter.

## Key symbols

- `def risk_level()`
- `def split_users()`
- `def calibrated_cutoffs()`
- `def youden_threshold()`
- `def fbeta_threshold()`
- `def cutoffs_for_method()`
- `def auc_metrics()`
- `def _label_scores()`
- `def _print_metrics()`
- `def _audit_source_rows()`
- `def _print_raw_feature_audit()`
- `def _print_calibration_diagnostics()`

## Connects to

- [[InSighter/notes/cert_adapter|cert_adapter.py]
- [[InSighter/notes/model|model.py]

## Used by

- [[InSighter/notes/test_cert_integration|test_cert_integration.py]

## Project modules

- [[InSighter/notes/app|app.py]
- [[InSighter/notes/auth|auth.py]
- [[InSighter/notes/cert_adapter|cert_adapter.py]
- [[InSighter/notes/cert_experiment|cert_experiment.py]
- [[InSighter/notes/database|database.py]
- [[InSighter/notes/generate_logs|generate_logs.py]
- [[InSighter/notes/ingestion|ingestion.py]
- [[InSighter/notes/llm_advisor|llm_advisor.py]
- [[InSighter/notes/model|model.py]
- [[InSighter/notes/privacy|privacy.py]
- [[InSighter/notes/role_baseline|role_baseline.py]
- [[InSighter/notes/sector_config|sector_config.py]
- [[InSighter/notes/simulation|simulation.py]
- [[InSighter/notes/test_ad_integration|test_ad_integration.py]
- [[InSighter/notes/test_auth_security|test_auth_security.py]
- [[InSighter/notes/test_cert_experiment|test_cert_experiment.py]
- [[InSighter/notes/test_cert_integration|test_cert_integration.py]
- [[InSighter/notes/test_ci_scripts|test_ci_scripts.py]
- [[InSighter/notes/test_compliance_rbac|test_compliance_rbac.py]
- [[InSighter/notes/test_desktop_async|test_desktop_async.py]
- [[InSighter/notes/test_desktop_safety|test_desktop_safety.py]
- [[InSighter/notes/test_hardening_logging|test_hardening_logging.py]
- [[InSighter/notes/test_llm_performance|test_llm_performance.py]
- [[InSighter/notes/test_model_calibration|test_model_calibration.py]
- [[InSighter/notes/test_role_baseline_setup_tab|test_role_baseline_setup_tab.py]
- [[InSighter/notes/test_role_baselines|test_role_baselines.py]
- [[InSighter/notes/test_sector_deployment|test_sector_deployment.py]
- [[InSighter/notes/test_sector_removal|test_sector_removal.py]
- [[InSighter/notes/test_sector_ui|test_sector_ui.py]
- [[InSighter/notes/test_support|test_support.py]
- [[InSighter/notes/test_uav_config_tab|test_uav_config_tab.py]

## Related

- [[CERT Dataset and Baselines|CERT Dataset & Baselines]]
- [[InSighter Hub]]
- File: [InSighter/source/cert_score.py](InSighter/source/cert_score.py)
