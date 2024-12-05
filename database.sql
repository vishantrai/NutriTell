CREATE DATABASE nutritell
CREATE TABLE indian_dishes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dish_name VARCHAR(255) NOT NULL,
    calories FLOAT NOT NULL, -- Calories per 100g
    protein FLOAT NOT NULL,  -- Protein per 100g in grams
    carbs FLOAT NOT NULL,    -- Carbohydrates per 100g in grams
    fat FLOAT NOT NULL       -- Fat per 100g in grams
);
INSERT INTO indian_dishes (dish_name, calories, protein, carbs, fat)
VALUES
    ('Chhole Bhature', 295, 8.0, 39.0, 11.0),
    ('Aaloo Paratha', 210, 4.0, 31.0, 7.0),
    ('Chicken Curry', 150, 20.0, 3.0, 7.0),
    ('Biryani', 240, 8.0, 33.0, 8.0),
    ('Puri Sabji', 250, 5.0, 30.0, 12.0),
    ('Dosa', 168, 4.0, 36.0, 3.0),
    ('Idli', 120, 2.5, 24.0, 1.5),
    ('Paneer Butter Masala', 270, 9.0, 12.0, 21.0),
    ('Rajma Chawal', 198, 7.0, 32.0, 4.0),
    ('Dal Tadka', 120, 6.0, 16.0, 4.0),
    ('Samosa', 262, 4.0, 35.0, 12.0),
    ('Pav Bhaji', 250, 5.0, 37.0, 8.0),
    ('Masala Dosa', 220, 5.0, 35.0, 6.0),
    ('Roti Sabji', 180, 4.0, 28.0, 4.0),
    ('Fish Curry', 140, 19.0, 3.0, 6.0),
    ('Keema Naan', 270, 12.0, 32.0, 10.0),
    ('Palak Paneer', 190, 7.0, 12.0, 14.0),
    ('Veg Pulao', 150, 3.0, 25.0, 3.0),
    ('Kheer', 140, 3.0, 25.0, 4.0),
    ('Gajar Halwa', 250, 4.0, 30.0, 12.0);
