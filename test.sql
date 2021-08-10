SELECT * FROM raterprojectapi_category;
SELECT * FROM raterprojectapi_gamecategory;
SELECT * FROM raterprojectapi_rating;

SELECT id FROM raterprojectapi_rating
WHERE id > 4;

DELETE FROM raterprojectapi_rating
WHERE id > 4;