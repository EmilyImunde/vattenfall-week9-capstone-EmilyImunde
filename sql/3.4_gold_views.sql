CREATE OR REPLACE VIEW vattenfall_dev.analytics.vw_regional_operations_dashboard AS
SELECT *
FROM vattenfall_dev.analytics.gold_regional_operations_dashboard;

CREATE OR REPLACE VIEW vattenfall_dev.analytics.vw_daily_incident_trends AS
SELECT
    event_day,
    region,
    severity_band,
    incident_count,
    elevated_incident_count,
    total_duration_minutes,
    avg_duration_minutes,
    affected_asset_count,
    operational_status
FROM vattenfall_dev.analytics.gold_grid_incident_summary;

CREATE OR REPLACE VIEW vattenfall_dev.analytics.vw_market_weather_overview AS
SELECT
    m.report_day,
    m.region,
    m.avg_price_eur_mwh,
    m.max_price_eur_mwh,
    m.total_volume_mwh,
    m.is_high_market_price,
    w.avg_temperature_c,
    w.avg_wind_speed_kmh,
    w.max_wind_speed_kmh,
    w.total_precipitation_mm,
    w.weather_alert_count,
    w.weather_risk_signal
FROM vattenfall_dev.analytics.gold_daily_market_summary m
LEFT JOIN vattenfall_dev.analytics.gold_weather_impact_summary w
    ON m.report_day = w.report_day
    AND m.region = w.region;