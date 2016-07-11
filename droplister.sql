/*
Navicat MySQL Data Transfer

Source Server         : MyHost
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : droplister

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-07-11 19:33:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` text NOT NULL,
  `paypal_email` text,
  `token` text NOT NULL,
  `token_expiration_date` date NOT NULL,
  `ebay_user_id` text NOT NULL,
  `site_code` text NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('1', 'allfyou@hotmail.com', 'allfyou@hotmail.com', 'AgAAAA**AQAAAA**aAAAAA**h+d+Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/', '2017-12-29', 'testuser_david123', 'US', '1');
INSERT INTO `account` VALUES ('2', 'allfyou@hotmail.com', 'allfyou@hotmail.com', 'AgAAAA**AQAAAA**aAAAAA**hTmAVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/', '2017-12-30', 'testuser_david123', 'US', '2');

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('ba9adbea27c5');

-- ----------------------------
-- Table structure for droplister_item
-- ----------------------------
DROP TABLE IF EXISTS `droplister_item`;
CREATE TABLE `droplister_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asin` varchar(255) NOT NULL,
  `title` text,
  `description` text,
  `amazon_price` float DEFAULT NULL,
  `image_url` text,
  `ebay_item_id` text,
  `ebay_price` float DEFAULT NULL,
  `site_code` varchar(20) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `amazon_offer_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asin` (`asin`),
  UNIQUE KEY `amazon_offer_id` (`amazon_offer_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `droplister_item_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of droplister_item
-- ----------------------------
INSERT INTO `droplister_item` VALUES ('2', 'B00XHK3B2E', 'ASICS Women\'s Gel-venture 5 Running Shoe, Black/Aqua Mint/Flash Coral, 8.5 M US', 'Description test', '56.71', 'http://ecx.images-amazon.com/images/I/51GsC3-b3oL._SL75_.jpg', '1101806947891', '66.71', 'US', '1', '2', 'vt2izcegNGri%2Fya0kqnW18AJwdThVzotYdzPBw8OWJ%2FxaBcOrkBBs8J6jPo8w4L%2BX5iXCBwIFEAqwOe30FrZDVETMq52%2B0wQXaObLJbJdIX8gNqOrhSbgg%3D%3D');
INSERT INTO `droplister_item` VALUES ('3', 'B018JSOPFU', 'Dream Pairs 151009-M Men\'s Summer Mesh Light Weight Flexible Athletic Easy Walki', 'Description test', '23.38', 'http://ecx.images-amazon.com/images/I/41fqgvhVhBL._SL75_.jpg', '1104609747891', '33.38', 'US', '1', '2', 'vt2izcegNGpQCAAHEC56AcI0ZPVX2xJzVNIKF1tJX39aZs4TvHLgj0cEdbwEfZg%2BEM9jFpFKERfoMvYNLJqMvbRj%2F3HUDwuQrXm4bz%2FDgK6m%2FNxMg7dAhualuh48WpIEQtPT7OvC37Qv6wGPeIgX66H9t4RCmOGc');
INSERT INTO `droplister_item` VALUES ('4', 'B0197WRI92', 'DoGeek Unisex Hombres Mujeres 7 colores LED Light Up Zapatos Blanco Negro', 'Description test', '25.59', 'http://ecx.images-amazon.com/images/I/41t-banE21L._SL75_.jpg', '1104604947891', '35.59', 'US', '1', '2', '2YdVxWww3THoBrMPrkWs8vj7J35z3zrkZlFRK5Pq%2FjT33%2BA2cft2fRRVo4fqXhRGfHenZnY9zBIm4Rqg54OPHyQElf8BboDJ8L1TOb4EJ2BwWrvyKUZQtmbU5q8%2FJs026uE1xQIdoNE6hyUB3UFrGxCBvZpc6UKm');
INSERT INTO `droplister_item` VALUES ('5', 'B00KHWCWXY', 'Groundwork GR86 Zapatos de Seguridad de Cuero, Unisex, Azul (Navy/Yellow), 46 EU', 'Description test', '29.77', 'http://ecx.images-amazon.com/images/I/41FT6%2Bbvr2L._SL75_.jpg', '110460947891', '39.77', 'US', '1', '2', 'V%2FQpAffAQzKbsvxkBGxJ6Jfzf5B6p7%2BKTTJN8E07LpY0XN8KHyxzfnpE0dJOZt%2FuHS5QA59F6H5djNQle%2BC51Suh19P48di1RTJp7Hg5vRASI0eqc%2BFlHQ%3D%3D');
INSERT INTO `droplister_item` VALUES ('6', 'B01938MEJY', 'BM FootwearHerrenschuhe - Zapatos Derby Hombre\n, color Azul, talla 44', 'Description test', '23.05', 'http://ecx.images-amazon.com/images/I/4110LoB6X1L._SL75_.jpg', '110460947891', '33.05', 'US', '1', '2', 'V%2FQpAffAQzK8Kqrreu0cfGJz%2F%2B7kc%2F1794Yk1cKGe22DoKGq41yEw9kMGSE57gW04qKFDXY8yraY6ZqifWTHe%2BZEoBW2erVz6mZpQkuS8y%2F7ZDRT3s%2BZ1W7FaTMn1n4r');

-- ----------------------------
-- Table structure for droplister_order
-- ----------------------------
DROP TABLE IF EXISTS `droplister_order`;
CREATE TABLE `droplister_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ebay_order_id` varchar(255) NOT NULL,
  `ebay_quantity_purchased` int(11) DEFAULT NULL,
  `ebay_checkout_status` varchar(255) DEFAULT NULL,
  `ebay_order_status` varchar(255) DEFAULT NULL,
  `ebay_transaction_currency` varchar(100) DEFAULT NULL,
  `ebay_transaction_price` float DEFAULT NULL,
  `ebay_shipping_method` varchar(255) DEFAULT NULL,
  `ebay_shipping_currency` varchar(255) DEFAULT NULL,
  `ebay_shipping_value` varchar(255) DEFAULT NULL,
  `ebay_total_price` float DEFAULT NULL,
  `amazon_order_id` varchar(255) DEFAULT NULL,
  `amazon_order_status` varchar(255) DEFAULT NULL,
  `droplister_item_id` int(11) NOT NULL,
  `amazon_purchase_link` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ebay_order_id` (`ebay_order_id`),
  UNIQUE KEY `amazon_order_id` (`amazon_order_id`),
  KEY `droplister_item_id` (`droplister_item_id`),
  CONSTRAINT `droplister_order_ibfk_1` FOREIGN KEY (`droplister_item_id`) REFERENCES `droplister_item` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of droplister_order
-- ----------------------------
INSERT INTO `droplister_order` VALUES ('1', '110180947891-0', '1', 'Incomplete', 'Active', 'USD', '5', 'Other', 'USD', '5', '10', null, 'AMAZON_STATUS_REQUESTED', '5', 'https://www.amazon.es/gp/cart/aws-merge.html?cart-id=278-1861997-2461801%26associate-id=carlitossanfe-20%26hmac=2crrpfkdEaoIyh9RSmU4Wav4YEs%3D%26SubscriptionId=AKIAJ7NR4H5C4QHEHOWQ%26MergeCart=False');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of role
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pwdhash` varchar(255) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', null, 'admin@gmail.com', 'pbkdf2:sha1:1000$ohz8qfs4$485bc573a9d9c43af12f203493a33f5fab101923', '1');
INSERT INTO `user` VALUES ('2', 'David', 'Mtnez', 'allfyou@hotmail.com', 'pbkdf2:sha1:1000$EEpkUbvc$4783dd2c629015e5ebf6a1a8f830fa0ed82657df', '0');

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_role
-- ----------------------------
