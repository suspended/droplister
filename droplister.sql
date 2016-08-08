-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: droplister
-- ------------------------------------------------------
-- Server version	5.5.49-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'allfyou@hotmail.com','allfyou@hotmail.com','AgAAAA**AQAAAA**aAAAAA**h+d+Vw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/','2017-12-29','testuser_david123','US',1),(2,'allfyou@hotmail.com','allfyou@hotmail.com','AgAAAA**AQAAAA**aAAAAA**hTmAVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GgDZaKogWdj6x9nY+seQ**zdEDAA**AAMAAA**ngXV46TF7Es/oMef4vA5L73xrHZd8F4PYknX2BudjF9dxX+YILaoi0ipWHURtoRj2P8mOBNlxi5pupEqjKyKkBxE72VfgZuTDUBpbj03p0BM4UQ5+SfNytfR5FThkvtGEPD6vHmhP2MfMfcrDrsfpIRpdCpvEohphzcRB+hlr4bzlx4JV1p/umV963wj/RifUrnpOAuo2WopRsSVO7l+Z2R1sbK5SLUrQ44L3tctCxqce7SNan0wdhPiej5vzO612IQUEVO9gq34UPCMr4p9GWshNiixyk6NU/6IzB84vq+M5C91wrNwoQ1pNhme4qbShEOsNnAMeub7m4cz1BweC1Vkv8mEIIxCV1sEEUZPCGtSf7urtoZnGnhPkbiXXpFEoNFW6koN/x1EuZPxYcTf3Za7UvUd2U6sNVgLcS4eSq2S7wJLBH8jBbGBS54FVzq9dz9KcAtUmvPGKBVw7sbFgeCtQ8JRBNWHsbLBQQTdUL6296cGgmsDmQl2zL3hBsmEEBJdhin9+upcUyv47hVF+JUtxlzF8U5XmpXPBgkKr/5k468Jvyo5BLeriHdmjWL4GS6/cP/qNM7bC1jIsUntyj5V+mRtLomM98u4zo5HdfvUKSB3HaZx2tO4sGk+y5/kgrwNJRxxrqksAV0FaZ0ct/0SEmTwEQNR240npStebg6wjNiYoZXNVyYiOEsmklKeEfbud5G6eUK+OO/HZb2V479hLDsJA48fzz3wcvlXINQnLqIx2ehnovOKt7THxFv/','2017-12-30','testuser_david123','US',2),(3,'grandespreciosonline@hotmail.com','grandespreciosonline@hotmail.com','AgAAAA**AQAAAA**aAAAAA**3GaFVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6ABkIanDZeAoQmdj6x9nY+seQ**JFsDAA**AAMAAA**eYxIh5woiB1+Psa954c0c2ak3+/bIbiA3ZsTUPCyeM24jUX2ZFXOwt2iOXSKZUxIJM4sKR9X9vmtdDY6JJsEbKC2vVL0HCVG3t4UK5QdFOBTlwXEJ41GmTF9TpQ+8dXrIrlPdaWuVXKdWyHPK4dtgu1Fmd7Ct3N+B+10doT5kTJCtfoNfsvgBhDs+8qKGenlgCXUhe1FCKGTw4F9bdvB/j4b6zwXzcJzA/FGNtAXi/9CIaHNvQLFdb01t0isLrktaDb+XXzHHiqbrMzRN61eeq1gMVIzldAYBhNmFU4sjVPNeDqLN/qGs1rGOi+Elrh3kn3Lmv//TDSSCPK1I41vc7dAKZ1dDtkJfD7BGbAG3sPZfITY26kW074DO/sxxYNk2sIvAIzDMM/wnf+li889OXedDOgOGEhDEapQdgvuEvA+mQehhD4vlbvwPJfmA15ycpxGLzJCAwgWqF5FZ2LWbniUOmtz6dN3OVUYYNsfOeGE7h6I0bcm+Jnd+8xfvGI5Qd1mtN9hbO1jIu8X/+eV3wA4T3nYymnkY6tB92VlBZcGwCI9x1jSXALluaiVPKZDTtMZQgk9/f20hOEnQ/MGw8YdQhYBa+Sc3RWJEfs6KFdtC/B5tAb6/myXzricnmUEbWS8wTXs3rvL2cpvIpjv4jpXDg/P3Jgs0JBHsG65q3KbVG6UTXkx0G5i4jAMcsmkTg8/Xi5k/GfW1ZjIjm4otx9W5WOZOaJJuSb8FtsBZMclGf2eZN9ghhckbu1wvdlC','2018-01-03','grandespreciosonlinepro','US',3),(4,'allforyouint@hotmail.com','allforyouint@hotmail.com','AgAAAA**AQAAAA**aAAAAA**OQOpVw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AEkoehCZWFogudj6x9nY+seQ**JFsDAA**AAMAAA**XJTl/uMFy7G4JFkNfNhETuLTk77/RS9jtN0YqAmc6K60Km+Ua1PVWyNJanAPObWqNc53XEzzdIw5Eir4XX3HCASAU8qenXOg6YL7yR7cBkMP8qJUjoZNTiOZk0qQWy+Kd6o8tqezwy85mxr2HSevalzx1avI9M9/DtZ1+k8f8fQX+lIQ+Lbx+yjWMb8swv3lR7CJvld9sVANXWsyr6xmXbh6xTpJZbyJA/W2xmB1M5IGDd4gGZDf5reRx6RBlZU/vAfGsy1vHY5Gqxdyvu2Y0Ujo0g6Lo+1OqvVi7bau4ez+TLLbz4pPPYVOhBjf/bL6hiGii5LMFSrdb7iQPDPrZev68S7H4BdmTWxe2yh1xWBeq0mc0veRZs7W9Ic3XtW8+65jXXwLgq2K1lVV1f2DH6S9Lm5+H2zT0berYrUp+00ZKz/YHjsH2H+WDMZkeMOB4MrMPXI3Fu9gxigpUd1twgnCcKAZh4e77s3y2FjMZbFb5mN4et+067ozTz6r2aVbu5OI0wVVM2Pz5CumuYvFLzUguQkLJYeSh8XBmjXnUCgGxAVU/cu4en7epYeP+xZONul1q63WE9JMoivXoch8ON069NYlKKSO+BU9qx0ber1PAYZywQvvwM0dBFlKIfWhseRTsCb0SL4Yv5Udfk825+kJoWCTTsGmpPdu0EWHY7sPSyA5KVrUKC/OMxwrS2T38DWJXd7LJv11J+xjxUUUwiI0fTBv7YUDDj1ASmA6dQqOHX1x9ilnZJKDcskgytf6','2018-01-30','iphonemedia','US',5);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('ba9adbea27c5');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `droplister_item`
--

DROP TABLE IF EXISTS `droplister_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `droplister_item`
--

LOCK TABLES `droplister_item` WRITE;
/*!40000 ALTER TABLE `droplister_item` DISABLE KEYS */;
INSERT INTO `droplister_item` VALUES (2,'B00XHK3B2E','ASICS Women\'s Gel-venture 5 Running Shoe, Black/Aqua Mint/Flash Coral, 8.5 M US','Description test',56.71,'http://ecx.images-amazon.com/images/I/51GsC3-b3oL._SL75_.jpg','1101806947891',66.71,'US',1,2,'vt2izcegNGri%2Fya0kqnW18AJwdThVzotYdzPBw8OWJ%2FxaBcOrkBBs8J6jPo8w4L%2BX5iXCBwIFEAqwOe30FrZDVETMq52%2B0wQXaObLJbJdIX8gNqOrhSbgg%3D%3D'),(3,'B018JSOPFU','Dream Pairs 151009-M Men\'s Summer Mesh Light Weight Flexible Athletic Easy Walki','Description test',23.38,'http://ecx.images-amazon.com/images/I/41fqgvhVhBL._SL75_.jpg','1104609747891',33.38,'US',1,2,'vt2izcegNGpQCAAHEC56AcI0ZPVX2xJzVNIKF1tJX39aZs4TvHLgj0cEdbwEfZg%2BEM9jFpFKERfoMvYNLJqMvbRj%2F3HUDwuQrXm4bz%2FDgK6m%2FNxMg7dAhualuh48WpIEQtPT7OvC37Qv6wGPeIgX66H9t4RCmOGc'),(4,'B0197WRI92','DoGeek Unisex Hombres Mujeres 7 colores LED Light Up Zapatos Blanco Negro','Description test',25.59,'http://ecx.images-amazon.com/images/I/41t-banE21L._SL75_.jpg','1104604947891',35.59,'US',1,2,'2YdVxWww3THoBrMPrkWs8vj7J35z3zrkZlFRK5Pq%2FjT33%2BA2cft2fRRVo4fqXhRGfHenZnY9zBIm4Rqg54OPHyQElf8BboDJ8L1TOb4EJ2BwWrvyKUZQtmbU5q8%2FJs026uE1xQIdoNE6hyUB3UFrGxCBvZpc6UKm'),(5,'B00KHWCWXY','Groundwork GR86 Zapatos de Seguridad de Cuero, Unisex, Azul (Navy/Yellow), 46 EU','Description test',29.77,'http://ecx.images-amazon.com/images/I/41FT6%2Bbvr2L._SL75_.jpg','110460947891',39.77,'US',1,2,'V%2FQpAffAQzKbsvxkBGxJ6Jfzf5B6p7%2BKTTJN8E07LpY0XN8KHyxzfnpE0dJOZt%2FuHS5QA59F6H5djNQle%2BC51Suh19P48di1RTJp7Hg5vRASI0eqc%2BFlHQ%3D%3D'),(6,'B01938MEJY','BM FootwearHerrenschuhe - Zapatos Derby Hombre\n, color Azul, talla 44','Description test',23.05,'http://ecx.images-amazon.com/images/I/4110LoB6X1L._SL75_.jpg','110460947891',33.05,'US',1,2,'V%2FQpAffAQzK8Kqrreu0cfGJz%2F%2B7kc%2F1794Yk1cKGe22DoKGq41yEw9kMGSE57gW04qKFDXY8yraY6ZqifWTHe%2BZEoBW2erVz6mZpQkuS8y%2F7ZDRT3s%2BZ1W7FaTMn1n4r');
/*!40000 ALTER TABLE `droplister_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `droplister_order`
--

DROP TABLE IF EXISTS `droplister_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `droplister_order`
--

LOCK TABLES `droplister_order` WRITE;
/*!40000 ALTER TABLE `droplister_order` DISABLE KEYS */;
INSERT INTO `droplister_order` VALUES (1,'110180947891-0',1,'Incomplete','Active','USD',5,'Other','USD','5',10,NULL,'AMAZON_STATUS_REQUESTED',5,'https://www.amazon.es/gp/cart/aws-merge.html?cart-id=278-1861997-2461801%26associate-id=carlitossanfe-20%26hmac=2crrpfkdEaoIyh9RSmU4Wav4YEs%3D%26SubscriptionId=AKIAJ7NR4H5C4QHEHOWQ%26MergeCart=False');
/*!40000 ALTER TABLE `droplister_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pwdhash` varchar(255) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin',NULL,'admin@gmail.com','pbkdf2:sha1:1000$ohz8qfs4$485bc573a9d9c43af12f203493a33f5fab101923',1),(2,'David','Mtnez','allfyou@hotmail.com','pbkdf2:sha1:1000$EEpkUbvc$4783dd2c629015e5ebf6a1a8f830fa0ed82657df',0),(3,'grandes','preciosonline','grandespreciosonline@hotmail.com','pbkdf2:sha1:1000$Xuv6rZOA$56a1723caec148435565e5ebd7451cbd1826bfa1',0),(5,'allforyou','int','allforyouint@hotmail.com','pbkdf2:sha1:1000$inq8Nb0B$4ed3d9d4cd63d3b242f528075285da97e1d54f0d',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_role` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-08 18:26:20
