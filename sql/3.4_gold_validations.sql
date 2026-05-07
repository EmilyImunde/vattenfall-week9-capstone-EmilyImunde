SELECT COUNT(*) AS row_count
FROM vattenfall_dev.analytics.gold_daily_market_summary;

SELECT COUNT(*) AS row_count
FROM vattenfall_dev.analytics.gold_weather_impact_summary;

SELECT COUNT(*) AS row_count
FROM vattenfall_dev.analytics.gold_grid_incident_summary;

SELECT COUNT(*) AS row_count
FROM vattenfall_dev.analytics.gold_regional_operations_dashboard;

SELECT report_day, region, COUNT(*) AS duplicate_count
FROM vattenfall_dev.analytics.gold_daily_market_summary
GROUP BY report_day, region
HAVING COUNT(*) > 1;

SELECT report_day, region, COUNT(*) AS duplicate_count
FROM vattenfall_dev.analytics.gold_weather_impact_summary
GROUP BY report_day, region
HAVING COUNT(*) > 1;

SELECT event_day, region, severity_band, COUNT(*) AS duplicate_count
FROM vattenfall_dev.analytics.gold_grid_incident_summary
GROUP BY event_day, region, severity_band
HAVING COUNT(*) > 1;

SELECT report_day, region, COUNT(*) AS duplicate_count
FROM vattenfall_dev.analytics.gold_regional_operations_dashboard
GROUP BY report_day, region
HAVING COUNT(*) > 1