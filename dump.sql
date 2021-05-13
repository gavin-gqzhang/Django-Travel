-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: travel
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attractions_datail`
--

DROP TABLE IF EXISTS `attractions_datail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attractions_datail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '景点名称',
  `address` varchar(255) DEFAULT NULL COMMENT '详细地址',
  `datail` text COMMENT '详情信息',
  `suggest` int(11) DEFAULT NULL COMMENT '是否推荐',
  `type` varchar(255) DEFAULT NULL COMMENT '景点类型',
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '邮箱',
  `phone` bigint(20) DEFAULT NULL COMMENT '电话',
  `max_num` int(11) DEFAULT NULL COMMENT '最大容纳人数',
  `max_price` float(10,2) DEFAULT NULL COMMENT '最高价格',
  `min_price` float(10,2) DEFAULT NULL COMMENT '最低价格',
  `in_time` varchar(255) DEFAULT NULL COMMENT '开放时间\n',
  `manager` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '管理员',
  `price` float(10,2) DEFAULT NULL COMMENT '价格',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attractions_datail`
--

LOCK TABLES `attractions_datail` WRITE;
/*!40000 ALTER TABLE `attractions_datail` DISABLE KEYS */;
INSERT INTO `attractions_datail` VALUES (4,'临沂大学','山东省临沂市兰山区临沂大学','',NULL,'None','123@qq.com',123,100,25.00,20.00,'8:00-20:00','ASDXZSDF',NULL);
/*!40000 ALTER TABLE `attractions_datail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attractions_img`
--

DROP TABLE IF EXISTS `attractions_img`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attractions_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attractions_id` int(11) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attractions_img`
--

LOCK TABLES `attractions_img` WRITE;
/*!40000 ALTER TABLE `attractions_img` DISABLE KEYS */;
/*!40000 ALTER TABLE `attractions_img` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attractions_order`
--

DROP TABLE IF EXISTS `attractions_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attractions_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attractions_id` int(11) DEFAULT NULL COMMENT '对应景点id',
  `user_id` int(11) DEFAULT NULL COMMENT '对应用户id',
  `price` float(10,2) DEFAULT NULL COMMENT '价格',
  `auth_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '下单时间',
  `use_time` varchar(255) DEFAULT NULL COMMENT '使用时间',
  `phone` varchar(255) DEFAULT NULL COMMENT '联系方式',
  `name` varchar(255) DEFAULT NULL COMMENT '使用人姓名',
  `num` int(11) DEFAULT NULL,
  `price_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attractions_order`
--

LOCK TABLES `attractions_order` WRITE;
/*!40000 ALTER TABLE `attractions_order` DISABLE KEYS */;
INSERT INTO `attractions_order` VALUES (1,4,15,25.00,'2019-12-17 18:46:35','2019-12-14','142456','zxasd',1,1),(2,4,15,50.00,'2019-12-18 18:46:35','2019-12-16','asdas','tdfgd',2,1),(3,4,15,25.00,'2019-12-18 18:46:35','2019-12-17','axzdsd','11fgd',1,1),(4,4,15,20.00,'2019-12-18 10:51:25','2019-12-18','152312','zgq',1,2),(5,4,15,25.00,'2019-12-20 05:17:14','2019-12-20','1235456','zha',1,1),(6,4,15,20.00,'2019-12-20 05:29:51','2019-12-20','12356','张国',1,2),(7,4,15,25.00,'2019-12-20 05:40:24','2019-12-22','12123','zzzzz',1,1),(8,4,15,50.00,'2019-12-20 05:45:47','2019-12-20','453123','zxzcxc',2,1),(9,4,15,75.00,'2019-12-20 05:55:33','2019-12-22','123131','45asd',3,1);
/*!40000 ALTER TABLE `attractions_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attractions_price`
--

DROP TABLE IF EXISTS `attractions_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attractions_price` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) DEFAULT NULL COMMENT '对应景点id',
  `ticket_name` varchar(255) DEFAULT NULL COMMENT '票名\n',
  `ticket_price` float(10,2) DEFAULT NULL COMMENT '票价\n',
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='景点票价';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attractions_price`
--

LOCK TABLES `attractions_price` WRITE;
/*!40000 ALTER TABLE `attractions_price` DISABLE KEYS */;
INSERT INTO `attractions_price` VALUES (1,4,'成人票',25.00,11),(2,4,'学生票',20.00,2);
/*!40000 ALTER TABLE `attractions_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 房间信息',7,'add_home_information'),(26,'Can change 房间信息',7,'change_home_information'),(27,'Can delete 房间信息',7,'delete_home_information'),(28,'Can view 房间信息',7,'view_home_information'),(29,'Can add 酒店信息',8,'add_information'),(30,'Can change 酒店信息',8,'change_information'),(31,'Can delete 酒店信息',8,'delete_information'),(32,'Can view 酒店信息',8,'view_information'),(33,'Can add 订单信息',9,'add_order'),(34,'Can change 订单信息',9,'change_order'),(35,'Can delete 订单信息',9,'delete_order'),(36,'Can view 订单信息',9,'view_order'),(37,'Can add 房间信息',10,'add_home_infor'),(38,'Can change 房间信息',10,'change_home_infor'),(39,'Can delete 房间信息',10,'delete_home_infor'),(40,'Can view 房间信息',10,'view_home_infor'),(41,'Can add 酒店详情',11,'add_hotel_datail'),(42,'Can change 酒店详情',11,'change_hotel_datail'),(43,'Can delete 酒店详情',11,'delete_hotel_datail'),(44,'Can view 酒店详情',11,'view_hotel_datail'),(45,'Can add 酒店房间信息',12,'add_hotel_infor'),(46,'Can change 酒店房间信息',12,'change_hotel_infor'),(47,'Can delete 酒店房间信息',12,'delete_hotel_infor'),(48,'Can view 酒店房间信息',12,'view_hotel_infor'),(49,'Can add 景点信息',13,'add_attractions'),(50,'Can change 景点信息',13,'change_attractions'),(51,'Can delete 景点信息',13,'delete_attractions'),(52,'Can view 景点信息',13,'view_attractions'),(53,'Can add 景点门票价格',14,'add_attractions_price'),(54,'Can change 景点门票价格',14,'change_attractions_price'),(55,'Can delete 景点门票价格',14,'delete_attractions_price'),(56,'Can view 景点门票价格',14,'view_attractions_price'),(57,'Can add 轮播图',15,'add_banner_img'),(58,'Can change 轮播图',15,'change_banner_img'),(59,'Can delete 轮播图',15,'delete_banner_img'),(60,'Can view 轮播图',15,'view_banner_img'),(61,'Can add 景点流量信息',16,'add_flow'),(62,'Can change 景点流量信息',16,'change_flow'),(63,'Can delete 景点流量信息',16,'delete_flow'),(64,'Can view 景点流量信息',16,'view_flow'),(65,'Can add 新闻',17,'add_news'),(66,'Can change 新闻',17,'change_news'),(67,'Can delete 新闻',17,'delete_news'),(68,'Can view 新闻',17,'view_news'),(69,'Can add 景点信息',18,'add_attractions_datail'),(70,'Can change 景点信息',18,'change_attractions_datail'),(71,'Can delete 景点信息',18,'delete_attractions_datail'),(72,'Can view 景点信息',18,'view_attractions_datail'),(73,'Can add 景点详情',19,'add_attractionsdatail'),(74,'Can change 景点详情',19,'change_attractionsdatail'),(75,'Can delete 景点详情',19,'delete_attractionsdatail'),(76,'Can view 景点详情',19,'view_attractionsdatail'),(77,'Can add 景点图片',20,'add_attractionsimg'),(78,'Can change 景点图片',20,'change_attractionsimg'),(79,'Can delete 景点图片',20,'delete_attractionsimg'),(80,'Can view 景点图片',20,'view_attractionsimg'),(81,'Can add 景区订单信息',21,'add_attractionsorder'),(82,'Can change 景区订单信息',21,'change_attractionsorder'),(83,'Can delete 景区订单信息',21,'delete_attractionsorder'),(84,'Can view 景区订单信息',21,'view_attractionsorder'),(85,'Can add 景点价格信息',22,'add_attractionsprice'),(86,'Can change 景点价格信息',22,'change_attractionsprice'),(87,'Can delete 景点价格信息',22,'delete_attractionsprice'),(88,'Can view 景点价格信息',22,'view_attractionsprice'),(89,'Can add auth group',23,'add_authgroup'),(90,'Can change auth group',23,'change_authgroup'),(91,'Can delete auth group',23,'delete_authgroup'),(92,'Can view auth group',23,'view_authgroup'),(93,'Can add auth group permissions',24,'add_authgrouppermissions'),(94,'Can change auth group permissions',24,'change_authgrouppermissions'),(95,'Can delete auth group permissions',24,'delete_authgrouppermissions'),(96,'Can view auth group permissions',24,'view_authgrouppermissions'),(97,'Can add auth permission',25,'add_authpermission'),(98,'Can change auth permission',25,'change_authpermission'),(99,'Can delete auth permission',25,'delete_authpermission'),(100,'Can view auth permission',25,'view_authpermission'),(101,'Can add auth user',26,'add_authuser'),(102,'Can change auth user',26,'change_authuser'),(103,'Can delete auth user',26,'delete_authuser'),(104,'Can view auth user',26,'view_authuser'),(105,'Can add auth user groups',27,'add_authusergroups'),(106,'Can change auth user groups',27,'change_authusergroups'),(107,'Can delete auth user groups',27,'delete_authusergroups'),(108,'Can view auth user groups',27,'view_authusergroups'),(109,'Can add auth user user permissions',28,'add_authuseruserpermissions'),(110,'Can change auth user user permissions',28,'change_authuseruserpermissions'),(111,'Can delete auth user user permissions',28,'delete_authuseruserpermissions'),(112,'Can view auth user user permissions',28,'view_authuseruserpermissions'),(113,'Can add django admin log',29,'add_djangoadminlog'),(114,'Can change django admin log',29,'change_djangoadminlog'),(115,'Can delete django admin log',29,'delete_djangoadminlog'),(116,'Can view django admin log',29,'view_djangoadminlog'),(117,'Can add django content type',30,'add_djangocontenttype'),(118,'Can change django content type',30,'change_djangocontenttype'),(119,'Can delete django content type',30,'delete_djangocontenttype'),(120,'Can view django content type',30,'view_djangocontenttype'),(121,'Can add django migrations',31,'add_djangomigrations'),(122,'Can change django migrations',31,'change_djangomigrations'),(123,'Can delete django migrations',31,'delete_djangomigrations'),(124,'Can view django migrations',31,'view_djangomigrations'),(125,'Can add django session',32,'add_djangosession'),(126,'Can change django session',32,'change_djangosession'),(127,'Can delete django session',32,'delete_djangosession'),(128,'Can view django session',32,'view_djangosession'),(129,'Can add 房间详情',33,'add_homedatail'),(130,'Can change 房间详情',33,'change_homedatail'),(131,'Can delete 房间详情',33,'delete_homedatail'),(132,'Can view 房间详情',33,'view_homedatail'),(133,'Can add 酒店详情',34,'add_hoteldatail'),(134,'Can change 酒店详情',34,'change_hoteldatail'),(135,'Can delete 酒店详情',34,'delete_hoteldatail'),(136,'Can view 酒店详情',34,'view_hoteldatail'),(137,'Can add 酒店图片',35,'add_hotelimg'),(138,'Can change 酒店图片',35,'change_hotelimg'),(139,'Can delete 酒店图片',35,'delete_hotelimg'),(140,'Can view 酒店图片',35,'view_hotelimg'),(141,'Can add 酒店订单信息',36,'add_hotelorder'),(142,'Can change 酒店订单信息',36,'change_hotelorder'),(143,'Can delete 酒店订单信息',36,'delete_hotelorder'),(144,'Can view 酒店订单信息',36,'view_hotelorder'),(145,'Can add 用户订单',37,'add_userorder'),(146,'Can change 用户订单',37,'change_userorder'),(147,'Can delete 用户订单',37,'delete_userorder'),(148,'Can view 用户订单',37,'view_userorder');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL DEFAULT '0',
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `is_staff` tinyint(1) DEFAULT '0',
  `is_active` tinyint(1) DEFAULT NULL,
  `date_joined` datetime(6) DEFAULT NULL,
  `hotel_user` int(11) DEFAULT NULL,
  `attractions_user` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'argon2$argon2i$v=19$m=512,t=2,p=2$d1RPQjM1cU9yUTFM$0C9PwB0r5AJAr5U+6N7RRQ/M/GH5KsgfBWaZkAEIx0=','2019-09-02 02:05:50.461053',1,'admin',1,1,'2019-09-01 02:30:26.876262',0,0,NULL),(12,'argon2$argon2i$v=19$m=512,t=2,p=2$d1RPQjM1cU9yUTFM$0C9PwB0r5AJAr5U+6N7RRQ','2019-12-20 05:56:17.236494',0,'SL668',0,NULL,'2019-09-11 16:44:53.480171',0,4,6),(13,'argon2$argon2i$v=19$m=512,t=2,p=2$d1RPQjM1cU9yUTFM$0C9PwB0r5AJAr5U+6N7RRQ','2019-12-20 05:57:31.306283',0,'puppet',0,NULL,'2019-09-11 16:45:54.198720',2,0,7),(15,'argon2$argon2i$v=19$m=512,t=2,p=2$N0RHZ0VPZU00eEtz$MeSpizVaZW6yhPzLLQeq1A','2019-12-20 05:54:30.515081',0,'test',0,NULL,'2019-12-07 07:04:26.379914',0,0,8);
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(13,'index','attractions'),(18,'index','attractions_datail'),(14,'index','attractions_price'),(19,'index','attractionsdatail'),(20,'index','attractionsimg'),(21,'index','attractionsorder'),(22,'index','attractionsprice'),(23,'index','authgroup'),(24,'index','authgrouppermissions'),(25,'index','authpermission'),(26,'index','authuser'),(27,'index','authusergroups'),(28,'index','authuseruserpermissions'),(15,'index','banner_img'),(29,'index','djangoadminlog'),(30,'index','djangocontenttype'),(31,'index','djangomigrations'),(32,'index','djangosession'),(16,'index','flow'),(10,'index','home_infor'),(7,'index','home_information'),(33,'index','homedatail'),(11,'index','hotel_datail'),(12,'index','hotel_infor'),(34,'index','hoteldatail'),(35,'index','hotelimg'),(36,'index','hotelorder'),(8,'index','information'),(17,'index','news'),(9,'index','order'),(37,'index','userorder'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-30 11:19:39.565249'),(2,'auth','0001_initial','2019-08-30 11:19:50.664745'),(3,'admin','0001_initial','2019-08-30 11:19:53.198724'),(4,'admin','0002_logentry_remove_auto_add','2019-08-30 11:19:53.236790'),(5,'admin','0003_logentry_add_action_flag_choices','2019-08-30 11:19:53.362692'),(6,'contenttypes','0002_remove_content_type_name','2019-08-30 11:19:54.902818'),(7,'auth','0002_alter_permission_name_max_length','2019-08-30 11:19:56.573952'),(8,'auth','0003_alter_user_email_max_length','2019-08-30 11:19:56.863758'),(9,'auth','0004_alter_user_username_opts','2019-08-30 11:19:57.010129'),(10,'auth','0005_alter_user_last_login_null','2019-08-30 11:19:57.992959'),(11,'auth','0006_require_contenttypes_0002','2019-08-30 11:19:58.039806'),(12,'auth','0007_alter_validators_add_error_messages','2019-08-30 11:19:58.112537'),(13,'auth','0008_alter_user_username_max_length','2019-08-30 11:19:59.063542'),(14,'auth','0009_alter_user_last_name_max_length','2019-08-30 11:19:59.987527'),(15,'index','0001_initial','2019-08-30 11:20:00.036321'),(16,'index','0002_home_infor_hotel_datail_hotel_infor','2019-08-30 11:20:00.102690'),(17,'index','0003_auto_20190830_1834','2019-08-30 11:20:00.169060'),(18,'sessions','0001_initial','2019-08-30 11:20:00.741967'),(19,'index','0004_auto_20190902_1948','2019-09-02 11:48:53.569404'),(20,'index','0005_auto_20190902_1954','2019-09-02 11:54:52.889449'),(21,'index','0006_auto_20190902_2001','2019-09-02 12:04:38.451302'),(22,'index','0007_auto_20190902_2004','2019-09-02 12:04:38.558630'),(23,'index','0008_auto_20190911_1955','2019-09-11 11:55:35.991299');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0m2qkbbydp6lcmiwiiujsod4zk7im4s6','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-18 02:24:31.230413'),('2228wol8n6ofjhm3o1yj5o8h79rldnz5','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-10-13 11:16:07.954085'),('2wfcmtyblh162lz0y1h2kc2zl72ew8xz','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-18 14:43:16.229936'),('2wlbetiyzbm3fljexty1zkzu967xs2ly','NDgyMjM4N2I0ZTc5NDJhMDIyYjE4YmMxYmQwYzhlMDZjMWMyMWJmZDp7InVzZXJuYW1lIjoidGVzdCJ9','2019-12-19 15:44:44.237419'),('364hqy0sjggkgjfmtge19kymsb42yp24','NDgyMjM4N2I0ZTc5NDJhMDIyYjE4YmMxYmQwYzhlMDZjMWMyMWJmZDp7InVzZXJuYW1lIjoidGVzdCJ9','2019-12-15 14:07:36.310413'),('4g62r3ldlago493o74ofyz5v0jushc79','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-14 08:01:00.646871'),('6x9rg9pmibzjymjdpsza3vl35m9ucfkf','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-18 06:05:00.222999'),('81j3k0f50dua2a3tkl2em0620hjmz3jq','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-20 06:28:21.930812'),('8zlxyxcmkqg3v3neo08n2ym7meapmz4s','NDgyMjM4N2I0ZTc5NDJhMDIyYjE4YmMxYmQwYzhlMDZjMWMyMWJmZDp7InVzZXJuYW1lIjoidGVzdCJ9','2019-12-15 11:30:36.226290'),('98km6tlto48uy9mqo52umz66brlg9lbr','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-10-15 09:34:08.436054'),('aw62tdo82o6wlay89hf6zys1eitjc3j6','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-17 10:31:40.387178'),('bft5pw3k9irfba3ng4komh11jq2y7s3l','ZjY2NDRlNDRjNzRhNWE5N2JhYmI3OGFjOTY1N2U0YjY4YWQ0MmEyZDp7fQ==','2019-12-19 13:44:09.519711'),('fbbmcjm47a2wsu1un6modwshzgle49zh','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-19 09:46:50.858858'),('gjo8xjrewbzd7uffszrs03ubkm0f557e','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-18 12:34:13.479504'),('iivm7xxuogs8sm3odikh9f72v9vwr3u5','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-07 08:11:21.512761'),('jjds1wsynjkcszo6u3k289nurubqk3gn','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-20 01:20:19.676140'),('lf36u5vy5z6c3gkdi54n7zufu4b1wn6m','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-17 12:59:27.789096'),('mogjl72lp60liy8duwxkggd0s92ciltg','NDgyMjM4N2I0ZTc5NDJhMDIyYjE4YmMxYmQwYzhlMDZjMWMyMWJmZDp7InVzZXJuYW1lIjoidGVzdCJ9','2019-12-16 07:45:10.803213'),('n2v80zblzbfil4am5fnndwfzzg5ss2o1','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-10-15 04:27:08.072014'),('nalsviiwc4mxcvoql12t0m9q6j74vutl','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-18 11:43:25.400192'),('o0lg197xsp4j7gc1fhdcre0g1u2ekidp','NDgyMjM4N2I0ZTc5NDJhMDIyYjE4YmMxYmQwYzhlMDZjMWMyMWJmZDp7InVzZXJuYW1lIjoidGVzdCJ9','2019-12-16 02:36:25.274985'),('tb123bhfwmu3v8j6am0m3s246ay44t58','NjBhZTQ1NDRkZDI2Nzc3ZTM4N2M1ZGFlZjQwYjgzN2I1M2QzZmM0Mjp7InVzZXJuYW1lIjoiU0w2NjgifQ==','2019-12-19 11:17:39.361511'),('tvcf11n3naq7irmjwbme83ehtxrkugn4','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-17 16:57:55.482000'),('v0cmbez2ib4xbpiix0goa3u1g7mtsgc4','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-12-20 04:55:21.034528'),('ywzvslqzp6wtmhxdhczzfaske0g01ftn','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-10-15 05:25:53.864336'),('z0y40si0divjxekr15kjzkkiikwzdoay','YmFlMWRiYjMyMGM5NWVlY2Y5YTM0YTlhM2QyMGUxOGU4YzkwM2RlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NzFkZjViNTdjMzljY2NiNDQyNTRiM2RhMzMxOWUyMWU4ODRjOTAwIn0=','2019-09-16 02:05:50.617181'),('zajy5en7pnxowlc4rr3xv4pb3vnhdr31','NDM5YjAxMjg4Zjk3NmExNTUwMDVhZDE5NWE1MmE0OTcwNmVjZjI1Nzp7InVzZXJuYW1lIjoicHVwcGV0In0=','2019-10-14 04:14:03.717533');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flow`
--

DROP TABLE IF EXISTS `flow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `flow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_id` int(11) DEFAULT NULL,
  `max` float DEFAULT NULL,
  `time1_flow` float DEFAULT NULL,
  `time2_flow` float DEFAULT NULL,
  `time3_flow` float DEFAULT NULL,
  `time4_flow` float DEFAULT NULL,
  `time5_flow` float DEFAULT NULL,
  `time6_flow` float DEFAULT NULL,
  `flow_img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flow`
--

LOCK TABLES `flow` WRITE;
/*!40000 ALTER TABLE `flow` DISABLE KEYS */;
INSERT INTO `flow` VALUES (1,4,100,50,70,50,90,10,100,'FlowImg/临沂大学_line.jpg');
/*!40000 ALTER TABLE `flow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_datail`
--

DROP TABLE IF EXISTS `home_datail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `home_datail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_id` int(11) DEFAULT NULL COMMENT '对应酒店id',
  `home` varchar(255) DEFAULT NULL COMMENT '房间类型',
  `person_num` int(11) DEFAULT NULL COMMENT '可容纳人数',
  `price` float(10,2) DEFAULT NULL COMMENT '房间价格',
  `num` int(11) DEFAULT NULL COMMENT '空房数量',
  `datail` text COMMENT '详情',
  `clean` int(11) DEFAULT NULL COMMENT '是否打扫',
  `get_person` int(11) DEFAULT NULL COMMENT '是否入住',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_datail`
--

LOCK TABLES `home_datail` WRITE;
/*!40000 ALTER TABLE `home_datail` DISABLE KEYS */;
INSERT INTO `home_datail` VALUES (1,2,'大床房',2,138.00,5,'大床房，有窗',NULL,NULL),(2,2,'双床房',2,120.00,7,'双床房，有窗',NULL,NULL);
/*!40000 ALTER TABLE `home_datail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_datail`
--

DROP TABLE IF EXISTS `hotel_datail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hotel_datail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager` varchar(255) DEFAULT NULL COMMENT '店长',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '酒店名称',
  `max_price` float(10,2) DEFAULT NULL COMMENT '酒店最高价',
  `min_price` float(10,2) DEFAULT NULL COMMENT '酒店最低价',
  `datail` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT '酒店介绍',
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '酒店地址',
  `phone` bigint(20) DEFAULT NULL COMMENT '联系电话',
  `price` float(10,2) DEFAULT NULL COMMENT '收益',
  `sum_order` int(11) DEFAULT NULL COMMENT '订单量',
  `home_num` int(11) DEFAULT NULL COMMENT '房间数',
  `in_time` varchar(255) DEFAULT NULL COMMENT '营业时间',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_datail`
--

LOCK TABLES `hotel_datail` WRITE;
/*!40000 ALTER TABLE `hotel_datail` DISABLE KEYS */;
INSERT INTO `hotel_datail` VALUES (2,'admin','蓝海国际',1100.00,100.00,'','山东省临沂市兰山区蓝海国际饭店',123456,NULL,NULL,15,'24小时','\'\'\'\'123456a@qq.com');
/*!40000 ALTER TABLE `hotel_datail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_img`
--

DROP TABLE IF EXISTS `hotel_img`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hotel_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `home_id` int(11) DEFAULT NULL,
  `hotel_id` int(11) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_img`
--

LOCK TABLES `hotel_img` WRITE;
/*!40000 ALTER TABLE `hotel_img` DISABLE KEYS */;
/*!40000 ALTER TABLE `hotel_img` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_order`
--

DROP TABLE IF EXISTS `hotel_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `hotel_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `hotel_id` int(11) DEFAULT NULL,
  `home_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL COMMENT '使用人姓名',
  `phone` varchar(255) DEFAULT NULL COMMENT '联系方式',
  `id_card` varchar(255) DEFAULT NULL COMMENT '身份证',
  `person` varchar(255) DEFAULT NULL COMMENT '居住人数',
  `data` varchar(255) DEFAULT NULL COMMENT '居住时间',
  `come_time` varchar(255) DEFAULT NULL COMMENT '预计到达时间',
  `live_time` varchar(255) DEFAULT NULL COMMENT '居住时间',
  `price` float(10,2) DEFAULT NULL COMMENT '价格',
  `auth_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_order`
--

LOCK TABLES `hotel_order` WRITE;
/*!40000 ALTER TABLE `hotel_order` DISABLE KEYS */;
INSERT INTO `hotel_order` VALUES (2,15,2,1,'zgq','135465','45213','1','1','21:30 - 22:00','2019-12-15',138.00,'2019-12-15 13:16:53'),(3,15,2,2,'zgq','456121','1231','1','1','14:30 - 15:00','2019-12-16',120.00,'2019-12-16 06:24:42'),(4,15,2,1,'卢富强','12312156','123456','1','1','22:30 - 23:00','2019-12-17',138.00,'2019-12-17 14:28:11'),(5,15,2,1,'nihao','1231321','12312','1','1','14:30 - 15:00','2019-12-20',138.00,'2019-12-20 05:13:18'),(6,15,2,1,'张国','12345','123','1','1','14:30 - 15:00','2019-12-20',138.00,'2019-12-20 05:29:08'),(7,15,2,1,'zzzz','45612312','12313','1','1','14:00 - 14:30','2019-12-21',138.00,'2019-12-20 05:39:31'),(8,15,2,2,'zzzzzzzzz','2135456','1231','1','1','16:00 - 16:30','2019-12-23',120.00,'2019-12-20 05:45:06'),(9,15,2,2,'dsfsd','312312','12312','1','1','19:00 - 19:30','2019-12-23',120.00,'2019-12-20 05:55:01');
/*!40000 ALTER TABLE `hotel_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL COMMENT '新闻标题',
  `summary` text COMMENT '新闻概况',
  `news_img` varchar(255) DEFAULT NULL COMMENT '新闻图片',
  `auth_time` time DEFAULT NULL COMMENT '新闻发布时间',
  `datail` text COMMENT '新闻详情',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publicity_photo`
--

DROP TABLE IF EXISTS `publicity_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `publicity_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_id` int(11) DEFAULT NULL COMMENT '酒店id',
  `attractions_id` int(11) DEFAULT NULL COMMENT '景点id',
  `upload` varchar(255) DEFAULT NULL COMMENT '宣传照路径',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publicity_photo`
--

LOCK TABLES `publicity_photo` WRITE;
/*!40000 ALTER TABLE `publicity_photo` DISABLE KEYS */;
INSERT INTO `publicity_photo` VALUES (1,NULL,4,'attractions\\临沂大学\\publicity_photo\\下载.jpg'),(2,2,NULL,'hotel\\蓝海国际\\下载.jpg');
/*!40000 ALTER TABLE `publicity_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_information`
--

DROP TABLE IF EXISTS `user_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `qq` varchar(255) DEFAULT NULL,
  `datail` text,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_information`
--

LOCK TABLES `user_information` WRITE;
/*!40000 ALTER TABLE `user_information` DISABLE KEYS */;
INSERT INTO `user_information` VALUES (5,NULL,123456,'123456789a@qq.com',NULL,NULL,NULL,NULL,NULL),(6,NULL,123,'123@qq.com',NULL,NULL,NULL,NULL,NULL),(7,NULL,123456,'123456a@qq.com',NULL,NULL,NULL,NULL,NULL),(8,NULL,1234567899,'123456@qq.com',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_order`
--

DROP TABLE IF EXISTS `user_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_order` int(11) DEFAULT NULL,
  `attraction_order` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_order`
--

LOCK TABLES `user_order` WRITE;
/*!40000 ALTER TABLE `user_order` DISABLE KEYS */;
INSERT INTO `user_order` VALUES (1,2,NULL,15),(2,NULL,1,15),(3,3,NULL,15),(4,NULL,2,15),(5,NULL,3,15),(6,4,NULL,15),(7,NULL,4,15),(8,5,NULL,15),(9,NULL,5,15),(10,6,NULL,15),(11,NULL,6,15),(12,7,NULL,15),(13,NULL,7,15),(14,8,NULL,15),(15,NULL,8,15),(16,9,NULL,15),(17,NULL,9,15);
/*!40000 ALTER TABLE `user_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-22 19:49:05
