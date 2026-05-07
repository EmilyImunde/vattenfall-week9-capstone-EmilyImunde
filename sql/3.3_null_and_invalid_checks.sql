SELECT COUNT(*) AS null_region_market_prices
FROM vattenfall_dev.refined.silver_market_prices
WHERE region IS NULL;

SELECT COUNT(*) AS invalid_duration_grid_events
FROM vattenfall_dev.refined.silver_grid_events
WHERE duration_minutes < 0;