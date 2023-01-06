/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - shopnswift
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`shopnswift` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `shopnswift`;

/*Table structure for table `assign_table` */

DROP TABLE IF EXISTS `assign_table`;

CREATE TABLE `assign_table` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` int(11) NOT NULL,
  `agent_loginid` int(11) NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assign_id`,`bill_id`,`agent_loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `assign_table` */

insert  into `assign_table`(`assign_id`,`bill_id`,`agent_loginid`,`status`,`date`) values 
(7,5,5,'delivered','2021-09-07'),
(8,3,5,'delivered','2022-01-14');

/*Table structure for table `bank_account` */

DROP TABLE IF EXISTS `bank_account`;

CREATE TABLE `bank_account` (
  `bankid` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `bankname` varchar(50) NOT NULL,
  `ifsc` varchar(50) NOT NULL,
  `keyno` varchar(50) NOT NULL,
  `accountno` bigint(20) NOT NULL,
  `cash` int(11) NOT NULL,
  PRIMARY KEY (`bankid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bank_account` */

insert  into `bank_account`(`bankid`,`user_lid`,`bankname`,`ifsc`,`keyno`,`accountno`,`cash`) values 
(1,8,'canara','1234','12345',1234567,9498);

/*Table structure for table `billing` */

DROP TABLE IF EXISTS `billing`;

CREATE TABLE `billing` (
  `billno` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(55) NOT NULL,
  `userid` int(50) NOT NULL,
  `totalprice` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`billno`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `billing` */

insert  into `billing`(`billno`,`date`,`userid`,`totalprice`,`status`) values 
(3,'2022-01-14',8,2,'pending');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `billid` int(11) DEFAULT NULL,
  `productid` varchar(50) NOT NULL,
  `quantity` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`cart_id`,`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cart_id`,`billid`,`productid`,`quantity`,`price`,`type`) values 
(4,3,'2','2',2,'online');

/*Table structure for table `delivery_address` */

DROP TABLE IF EXISTS `delivery_address`;

CREATE TABLE `delivery_address` (
  `add_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`add_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_address` */

insert  into `delivery_address`(`add_id`,`bill_id`,`name`,`phone`,`post`,`email`) values 
(1,6,'akmaal','9187284843','2223','hdjajksf'),
(2,2,'sj','ss','dd','ss'),
(3,0,'jajs','jsjs','jsjs','jsjs'),
(4,0,'122','123','123','123'),
(5,0,'safvan','1123458','asdf','asdgg'),
(6,0,'qwerty','987654','poiuy','safuabisha@gmail.com'),
(7,0,'aa','sss','ss','sss'),
(8,0,'qwww','qww','ww','safuabisha@gmail.com'),
(9,0,'sham','sjjs','djjd','djjd');

/*Table structure for table `delivery_agent` */

DROP TABLE IF EXISTS `delivery_agent`;

CREATE TABLE `delivery_agent` (
  `agentid` int(11) NOT NULL AUTO_INCREMENT,
  `agent_loginid` int(11) NOT NULL,
  `agent_firstname` varchar(50) NOT NULL,
  `agent_lastname` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` int(11) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`agentid`,`agent_loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_agent` */

insert  into `delivery_agent`(`agentid`,`agent_loginid`,`agent_firstname`,`agent_lastname`,`place`,`pin`,`phone`,`email`) values 
(3,5,'Rizal','Kapat','calicut',676558,9874586585,'qweer@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'safuabi','safuabi','store'),
(4,'delivery','delivery','dagent'),
(5,'rizal','rizal','dagent'),
(7,'sales','sales','sales'),
(8,'safvan','safvan','user'),
(9,'delivery','123456','store'),
(10,'shameemm','87654321','user'),
(11,'aslam','asklam','store'),
(12,'aslam','aslam','store'),
(13,'safvan','safvan','store'),
(14,'shameem','shameem','sales');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(50) NOT NULL,
  `mfgdate` varchar(50) NOT NULL,
  `expdate` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `productimage` varchar(50) NOT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`productid`,`productname`,`mfgdate`,`expdate`,`price`,`productimage`) values 
(1,'Nutella','2021-09-10','2024-10-10',100,'download.jpg'),
(2,'Boomer','2021-09-08','2021-10-15',1,'8902433001482-600x619.png');

/*Table structure for table `product_quantity` */

DROP TABLE IF EXISTS `product_quantity`;

CREATE TABLE `product_quantity` (
  `pid` int(11) NOT NULL,
  `qty` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `product_quantity` */

insert  into `product_quantity`(`pid`,`qty`) values 
(1,448),
(2,159);

/*Table structure for table `qr` */

DROP TABLE IF EXISTS `qr`;

CREATE TABLE `qr` (
  `qrid` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) NOT NULL,
  `path` varchar(50) NOT NULL,
  PRIMARY KEY (`qrid`,`productid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `qr` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `ratingid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `userlogin_id` int(11) DEFAULT NULL,
  `rating` float NOT NULL,
  PRIMARY KEY (`ratingid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`ratingid`,`date`,`userlogin_id`,`rating`) values 
(1,'2021-09-08',8,5),
(2,'2022-01-14',8,5),
(3,'2022-01-14',8,3);

/*Table structure for table `registration` */

DROP TABLE IF EXISTS `registration`;

CREATE TABLE `registration` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  KEY `userid` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `registration` */

insert  into `registration`(`userid`,`loginid`,`name`,`mobile`,`email`) values 
(1,8,'Mohammad safvan',9947432770,'safusaff008@gmail.com'),
(2,10,'shameem',9847630028,'mandayappuramshameem@gmail');

/*Table structure for table `staffreg` */

DROP TABLE IF EXISTS `staffreg`;

CREATE TABLE `staffreg` (
  `staffid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `pin` int(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`staffid`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staffreg` */

insert  into `staffreg`(`staffid`,`fname`,`lname`,`age`,`gender`,`place`,`phone`,`pin`,`email`,`loginid`) values 
(1,'mohammad','safvan',19,'male','tirur',9947432770,676106,'safusafzz007@gmail.com',13),
(2,'Shameem','M',20,'male','calicut',9847630028,234567,'mandayappuramshameem@gmail.com',14);

/*Table structure for table `track table` */

DROP TABLE IF EXISTS `track table`;

CREATE TABLE `track table` (
  `track_id` int(11) NOT NULL AUTO_INCREMENT,
  `agent_loginid` int(11) DEFAULT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  PRIMARY KEY (`track_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `track table` */

insert  into `track table`(`track_id`,`agent_loginid`,`latitude`,`longitude`) values 
(1,4,'11.2570701','75.7845671'),
(2,5,'11.2570701','75.7845671'),
(3,8,'11.2577836','75.7845297');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
