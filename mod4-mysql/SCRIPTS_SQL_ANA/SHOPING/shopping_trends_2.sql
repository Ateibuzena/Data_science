DROP DATABASE shopping_trends;
CREATE database IF NOT EXISTS shopping_trends;
USE shopping_trends;
CREATE table customers (
	customer_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    age INT UNSIGNED,
    gender ENUM ( "Male", "Female", "Non-gender" ),
    location VARCHAR ( 100 ),
    subscription_status BOOL,
    preferred_payment_method  ENUM ( 'Venmo', 'Cash', 'Credit Card', 'PayPal', 'Bank Transfer', 'Debit Card' ),
    frequency_of_purchases ENUM ( 'Fortnightly', 'Weekly', 'Annually', 'Quarterly', 
    'Bi-Weekly', 'Monthly', 'Every 3 Months', 'Every 6 Months', 'Sporadic' ),
    PRIMARY KEY ( customer_id )
    );
    
CREATE table categories (
	category_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    category ENUM ( 'Clothing', 'Footwear', 'Outerwear', 'Accessories' ),
    PRIMARY KEY ( category_id )
	);

CREATE table payments (
	payment_method_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    payment_method ENUM ( 'Credit Card', 'Bank Transfer', 'Cash', 'PayPal', 'Venmo', 'Debit Card' ),
    PRIMARY KEY ( payment_method_id )
    );
    
CREATE table shipping (
	shipping_type_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    shipping_type ENUM ( 'Express', 'Free Shipping', 'Next Day Air', 'Standard', '2-Day Shipping', 'Store Pickup' ),
    PRIMARY KEY ( shipping_type_id )
    );
    
CREATE table items (
	item_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	item_purchased ENUM ( 'Blouse', 'Sweater', 'Jeans', 'Sandals', 'Sneakers', 'Shirt', 'Shorts', 'Coat', 'Handbag', 
		'Shoes', 'Dress', 'Skirt', 'Sunglasses', 'Pants', 'Jacket', 'Hoodie', 'Jewelry', 'T-shirt', 'Scarf', 'Hat', 
        'Socks', 'Backpack', 'Belt', 'Boots', 'Gloves' ),
	size ENUM ( 'L', 'S', 'M', 'XL' ),
	color ENUM ( 'Gray', 'Maroon', 'Turquoise', 'White', 'Charcoal', 'Silver', 'Pink', 'Purple', 'Olive', 
		'Gold', 'Violet', 'Teal', 'Lavender', 'Black', 'Green', 'Peach', 'Red', 'Cyan', 'Brown', 'Beige',
		'Orange', 'Indigo', 'Yellow', 'Magenta', 'Blue' ),
	season ENUM ( 'Winter', 'Spring', 'Summer', 'Fall' ),
	category_id INT UNSIGNED,
    PRIMARY KEY ( item_id ),
    FOREIGN KEY ( category_id ) REFERENCES categories ( category_id ) ON DELETE SET NULL
    );
    
CREATE table purchases (
	purchase_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    purchase_amount_usd INT UNSIGNED,   
    discount_applied BOOL,
	promo_code_used BOOL,
	previous_purchases INT UNSIGNED,
	customer_id INT UNSIGNED,
	item_id INT UNSIGNED,
	payment_method_id INT UNSIGNED,
	shipping_type_id INT UNSIGNED,
    PRIMARY KEY ( purchase_id ),
    FOREIGN KEY ( customer_id ) REFERENCES customers (customer_id) ON DELETE SET NULL,
    FOREIGN KEY ( item_id ) REFERENCES items (item_id) ON DELETE SET NULL,
    FOREIGN KEY ( payment_method_id ) REFERENCES payments (payment_method_id) ON DELETE SET NULL,
    FOREIGN KEY ( shipping_type_id ) REFERENCES shipping (shipping_type_id) ON DELETE SET NULL
    );
    
CREATE table reviews (
	review_id INT UNSIGNED AUTO_INCREMENT NOT NULL,
	customer_id INT UNSIGNED,
	item_id INT UNSIGNED,
	review_rating DECIMAL ( 2,1 ),
    PRIMARY KEY ( review_id ),
    FOREIGN KEY ( customer_id ) REFERENCES customers ( customer_id ) ON DELETE SET NULL,
    FOREIGN KEY ( item_id ) REFERENCES items ( item_id ) ON DELETE SET NULL
    );