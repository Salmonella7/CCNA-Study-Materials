---
title: test_desktop_async.py
aliases:
  - test_desktop_async.py
tags:
  - insighter
  - insighter/tests
type: source-module
module: test_desktop_async.py
path: InSighter/source/test_desktop_async.py
category: Tests
project: InSighter
---

# test_desktop_async.py

> [!info] Tests
> Source: `InSighter/source/test_desktop_async.py`
> InSighter project file — see [[InSighter Hub|the hub]] and [[Tests|Tests]].

## Purpose

Part of the **Tests** layer of InSighter.

## Key symbols

- `def wait_for()`
- `class SlowHandler — do_GET, log_message`
- `class ApiClientTransportTest — response, test_timeout_and_connection_errors_are_api_errors, test_all_http_methods_use_request_with_timeout, test_login_redirect_expires_session_once_across_multiple_failed_gets, test_login_redirect_expires_session_for_ai_post, test_html_200_is_unexpected_logged_and_does_not_mark_offline`
- `class AsyncUiTest — setUpClass, test_refresh_returns_immediately_and_deduplicates_inflight_call, test_login_is_async_and_emits_success_on_ui_thread, test_login_displays_api_error_message_without_raw_exception`

## Connects to

- [[InSighter/notes/desktop_app/__init__|desktop_app/__init__.py]

## Project modules

- [[InSighter/notes/app|app.py]
- [[InSighter/notes/auth|auth.py]
- [[InSighter/notes/cert_adapter|cert_adapter.py]
- [[InSighter/notes/cert_experiment|cert_experiment.py]
- [[InSighter/notes/cert_score|cert_score.py]
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

- [[Tests|Tests]]
- [[InSighter Hub]]
- File: [InSighter/source/test_desktop_async.py](InSighter/source/test_desktop_async.py)
