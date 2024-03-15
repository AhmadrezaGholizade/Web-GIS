-- -- Exc 1
-- -- Finding the Average distance between pharmacies 
-- SELECT AVG(distance) AS average_distance
-- FROM (
--     SELECT ST_Distance(r1.geom, r2.geom) AS distance
--     FROM (SELECT * FROM rasht_pois_free_1 WHERE fclass = 'pharmacy') r1
--     JOIN (SELECT * FROM rasht_pois_free_1 WHERE fclass = 'pharmacy') r2 ON r1.id != r2.id
-- ) AS distances;

-- -- Exc 2
-- -- Finding the 3 nearest Park to arbitraty point in city
-- SELECT ST_Distance(geom, ST_GeomFromText('POINT(376620.2 4126600.0)', 32639)) AS distance, name 
-- FROM rasht_landuse_a_free_1 WHERE fclass = 'park' ORDER BY distance LIMIT 3;

-- -- Buffers
-- SELECT ST_Buffer(geom, 500) 
-- FROM rasht_pois_a_free_1 
-- WHERE fclass in ('hospital', 'clinic');

-- -- Roads
-- SELECT * FROM rasht_roads_free_1;

-- -- Roads that are intersected with buffers.
-- SELECT road.geom
-- FROM (SELECT ST_Buffer(geom, 500) as geom FROM rasht_pois_a_free_1 
-- 	  WHERE fclass in ('hospital', 'clinic')) buffer
-- JOIN rasht_roads_free_1 road ON ST_Intersects(buffer.geom, road.geom)

-- -- Exc 3
-- -- Finding Percentage within buffer
-- WITH buffer_roads_count AS (
--     SELECT COUNT(*) AS count
--     FROM (SELECT ST_Buffer(geom, 500) as geom FROM rasht_pois_a_free_1 
-- 		  WHERE fclass in ('hospital', 'clinic')) buffer
--     JOIN rasht_roads_free_1 road ON ST_Intersects(buffer.geom, road.geom)
-- ),
-- total_roads_count AS (
--     SELECT COUNT(*) AS count FROM rasht_roads_free_1
-- )
-- SELECT 
--     (SELECT count FROM buffer_roads_count) AS roads_within_buffer_count,
--     (SELECT count FROM total_roads_count) AS total_roads_count,
--     (SELECT count FROM buffer_roads_count)::numeric / (SELECT count FROM total_roads_count) * 100.0 
-- 	 AS percentage_within_buffer;

-- -- hex to Text
-- SELECT ST_AsText(ST_GeomFromWKB(decode('01010000207F7F00003BDBEA753DC91641B44D421E927A4F41', 'hex')));
