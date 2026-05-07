SELECT COUNT(*) AS null_region_market_prices
FROM vattenfall_dev.refined.silver_market_prices
WHERE region IS NULL;

SELECT COUNT(*) AS invalid_duration_grid_events
FROM vattenfall_dev.refined.silver_grid_events
WHERE duration_minutes < 0;

SELECT COUNT(*) AS negative_wind_speed
FROM vattenfall_dev.refined.silver_weather
WHERE wind_speed_kmh < 0;

SELECT asset_id, COUNT(*) AS duplicate_count
FROM vattenfall_dev.refined.silver_asset_reference
GROUP BY asset_id
HAVING COUNT(*) > 1;