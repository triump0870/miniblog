-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 02, 2016 at 09:07 PM
-- Server version: 5.6.27-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `miniblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=70 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add tag', 7, 'add_tag'),
(20, 'Can change tag', 7, 'change_tag'),
(21, 'Can delete tag', 7, 'delete_tag'),
(22, 'Can add post', 8, 'add_post'),
(23, 'Can change post', 8, 'change_post'),
(24, 'Can delete post', 8, 'delete_post'),
(31, 'Can add project', 11, 'add_project'),
(32, 'Can change project', 11, 'change_project'),
(33, 'Can delete project', 11, 'delete_project'),
(34, 'Can add work', 12, 'add_work'),
(35, 'Can change work', 12, 'change_work'),
(36, 'Can delete work', 12, 'delete_work'),
(37, 'Can add site', 13, 'add_site'),
(38, 'Can change site', 13, 'change_site'),
(39, 'Can delete site', 13, 'delete_site'),
(40, 'Can add about', 14, 'add_about'),
(41, 'Can change about', 14, 'change_about'),
(42, 'Can delete about', 14, 'delete_about'),
(43, 'Can add skill', 15, 'add_skill'),
(44, 'Can change skill', 15, 'change_skill'),
(45, 'Can delete skill', 15, 'delete_skill'),
(46, 'Can add education', 16, 'add_education'),
(47, 'Can change education', 16, 'change_education'),
(48, 'Can delete education', 16, 'delete_education'),
(49, 'Can add music', 17, 'add_music'),
(50, 'Can change music', 17, 'change_music'),
(51, 'Can delete music', 17, 'delete_music'),
(52, 'Can add user data', 18, 'add_userdata'),
(53, 'Can change user data', 18, 'change_userdata'),
(54, 'Can delete user data', 18, 'delete_userdata'),
(55, 'Can add language', 19, 'add_language'),
(56, 'Can change language', 19, 'change_language'),
(57, 'Can delete language', 19, 'delete_language'),
(58, 'Can add conference', 20, 'add_conference'),
(59, 'Can change conference', 20, 'change_conference'),
(60, 'Can delete conference', 20, 'delete_conference'),
(61, 'Can add contact', 21, 'add_contact'),
(62, 'Can change contact', 21, 'change_contact'),
(63, 'Can delete contact', 21, 'delete_contact'),
(64, 'Can add image', 22, 'add_image'),
(65, 'Can change image', 22, 'change_image'),
(66, 'Can delete image', 22, 'delete_image'),
(67, 'Can add privacy', 23, 'add_privacy'),
(68, 'Can change privacy', 23, 'change_privacy'),
(69, 'Can delete privacy', 23, 'delete_privacy');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$OBu4hYPNDyTn$2dkvCP8QDOJPB/cRlSd5lxn2M+FSNK6n5/ZvjdK6n+U=', '2016-08-06 12:12:47.444573', 1, 'rohan', '', '', 'b4you0870@gmail.com', 1, 1, '2015-04-16 09:46:20'),
(2, 'pbkdf2_sha256$15000$8qVdpH7G1N9G$TDvjjYbXyPTFPRvZp0np7oRw/BKZB/SOFn7Jsd0dhXk=', '2015-04-28 09:22:31.000000', 0, 'avishek', 'Avishek', 'Chatterjee', 'write2avishek@gmail.com', 0, 1, '2015-04-28 09:22:31');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 2, 8),
(2, 2, 13),
(3, 2, 14),
(4, 2, 15),
(5, 2, 16),
(6, 2, 17),
(7, 2, 18),
(8, 2, 19),
(9, 2, 20),
(10, 2, 21),
(11, 2, 22),
(12, 2, 23),
(13, 2, 24),
(14, 2, 31),
(15, 2, 32),
(16, 2, 33),
(17, 2, 34),
(18, 2, 35),
(19, 2, 36),
(20, 2, 37),
(21, 2, 38),
(22, 2, 39),
(23, 2, 40),
(24, 2, 41),
(25, 2, 42),
(26, 2, 43),
(27, 2, 44),
(28, 2, 45),
(29, 2, 46),
(30, 2, 47),
(31, 2, 48),
(32, 2, 49),
(33, 2, 50),
(34, 2, 51),
(35, 2, 52),
(36, 2, 53),
(37, 2, 54),
(38, 2, 55),
(39, 2, 56),
(40, 2, 57),
(41, 2, 58),
(42, 2, 59),
(43, 2, 60);

-- --------------------------------------------------------

--
-- Table structure for table `blog_about`
--

CREATE TABLE IF NOT EXISTS `blog_about` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `blog_about`
--

INSERT INTO `blog_about` (`id`, `content`) VALUES
(1, 'Full stack software engineer with special expertise in APIs and web services. Comfortable implementing great user experiences, managing server side scalability and concurrency, designing database schemas and batch processing jobs, and deploying and admining servers. Experienced in building sophisticated distributed systems using REST web APIs. Product focused and deeply passionate about solving interesting problems.\r\n\r\nI have a deep interest in mobile development. Currently, pursuing iOS Developer Nanodegree on Udacity. Looking for some opportunity in iOS development.\r\n\r\nI actively contribute to open source projects (see my [GitHub profile](http://github.com/triump0870)) because it is a way to develop great software that benefits both the contributor and the community. I blog at [rohanroy.com](http://rohanroy.com).'),
(2, 'I want to discover my true potential in terms of: physicality, mentality and creativity. I want to persist until its perfect. I want to empty the tank.'),
(3, 'I believe that we get one beautiful shot at life, it''s a privilege to be here, and it''s never too late to make it count. Today is not over yet.');

-- --------------------------------------------------------

--
-- Table structure for table `blog_conference`
--

CREATE TABLE IF NOT EXISTS `blog_conference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `place` varchar(100) NOT NULL,
  `link` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `blog_conference`
--

INSERT INTO `blog_conference` (`id`, `name`, `place`, `link`, `date`, `status`) VALUES
(1, 'TCS Code Vita', 'Kalyani', 'https://campuscommune.tcs.com/intro/view_blog/codevita-2014-tcs-global-coding-contest', '2013-11-20', 'p'),
(2, 'DGPLug Summer Training', 'Online', 'http://dgplug.org/summertraining/', '2014-08-24', 'p'),
(3, 'Pycon India 2015', 'Bangalore', 'https://in.pycon.org/2015/', '2015-10-02', 'p'),
(4, 'DjangoCon Europe 2016', 'Budapest', 'https://2016.djangocon.eu/', '2016-03-30', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `blog_contact`
--

CREATE TABLE IF NOT EXISTS `blog_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(70) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `blog_education`
--

CREATE TABLE IF NOT EXISTS `blog_education` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(30) NOT NULL,
  `institution` varchar(50) NOT NULL,
  `website` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `mode` varchar(20) NOT NULL,
  `status` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `blog_education`
--

INSERT INTO `blog_education` (`id`, `course`, `institution`, `website`, `start_date`, `end_date`, `mode`, `status`) VALUES
(1, 'Computer Science', 'Kalyani Govt. Engineering College', 'http://kgec.edu.in/', '2010-08-04', '2014-06-04', 'B.Tech', 'p'),
(2, 'Web Development', 'Udacity', 'https://www.udacity.com/course/cs253', '2014-08-20', '2015-04-12', '', 'p'),
(3, 'Full Stack Developer', 'Udacity', 'https://www.udacity.com/course/nd004', '2015-02-23', '2016-02-11', 'Nanodegree', 'p');

-- --------------------------------------------------------

--
-- Table structure for table `blog_image`
--

CREATE TABLE IF NOT EXISTS `blog_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `about_image` varchar(100) DEFAULT NULL,
  `contact_image` varchar(100) DEFAULT NULL,
  `postlist_image` varchar(100) DEFAULT NULL,
  `projectlist_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `blog_image`
--

INSERT INTO `blog_image` (`id`, `about_image`, `contact_image`, `postlist_image`, `projectlist_image`) VALUES
(1, 'images/1434016747-8c86c7d8-0a28-4f59-861c-6981638c1fa7.jpg', 'contact/1434016747-9f0f0279-bfbc-4c70-9d0a-0c495a2f207c.jpg', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `blog_language`
--

CREATE TABLE IF NOT EXISTS `blog_language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(70) NOT NULL,
  `proficiency` int(11) NOT NULL,
  `star` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `blog_language`
--

INSERT INTO `blog_language` (`id`, `language`, `proficiency`, `star`) VALUES
(1, 'Bengali', 1, 'xxxxx'),
(2, 'English', 2, 'xxxx'),
(3, 'Hindi', 2, 'xxxx');

-- --------------------------------------------------------

--
-- Table structure for table `blog_music`
--

CREATE TABLE IF NOT EXISTS `blog_music` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `music` varchar(255) NOT NULL,
  `url` varchar(200) NOT NULL,
  `status` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `blog_music`
--

INSERT INTO `blog_music` (`id`, `music`, `url`, `status`) VALUES
(1, 'We Code Hard', 'https://www.youtube.com/watch?v=KC8lt--rEEo', '1'),
(2, 'Until The Morning', 'https://www.youtube.com/watch?v=gvlNy8CdlIY', '1'),
(3, 'Muse - Uprising', 'https://www.youtube.com/watch?v=w8KQmps-Sog', '1'),
(4, 'End Of Line', 'https://www.youtube.com/watch?v=AHGvaQMClEo', '1');

-- --------------------------------------------------------

--
-- Table structure for table `blog_post`
--

CREATE TABLE IF NOT EXISTS `blog_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `url` varchar(250) NOT NULL,
  `author_id` int(11) NOT NULL,
  `status` varchar(1) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `blog_post_4f331e2f` (`author_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `blog_post`
--

INSERT INTO `blog_post` (`id`, `created_at`, `updated_at`, `title`, `slug`, `content`, `url`, `author_id`, `status`, `image`) VALUES
(1, '2015-04-16 09:52:40', '2016-07-19 21:16:24', 'my first django app', 'my-first-django-app', 'Wow!  what a big feeling, I''m going to write my first blog in my hand build personal blog. Actually, its my first Django application that I ran on Internet. So, how it became reality I''m going to tell you next.\r\n\r\n**Why Django**\r\n\r\nMany of my friends asked me why you selected Django over already existed renowned technologies like WordPress, Drupal etc. I simply replied I''m not interested on other technologies which are not robust like Django. Honestly saying I''m a Python programmer, so, why do I choose other technology other than Django ? As you all know Django rightnow is a hot favorite framework for web development in Python.\r\n\r\n**Setup**\r\n\r\nFirst I thought of using Amazon BeanStalk but didn''t able to setup correctly my Django app there. Finally, I used my most reliable source for development and hosting - the AWS EC2.\r\n    I used Virtualenv to create an isolated development setup for Django. But do you know Django isn''t capable of handling multithreading in a production server as it is single threaded application which is suitable for development purpose only. But Gunicorn server is capable of handling multiple requests at the sametime. To manage Gunicorn I used Supervisor which makes sure Gunicorn will always keep running.\r\n\r\n_**To be continued**_\r\n\r\n<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-in.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=IN&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=rohanroycom-21&marketplace=amazon&region=IN&placement=B01BKN1P2C&asins=B01BKN1P2C&linkId=&show_border=true&link_opens_in_new_window=true">\r\n</iframe>', '', 1, 'p', ''),
(2, '2015-04-19 12:27:13', '2016-07-19 20:38:17', 'My Personal blog building experience', 'my-personal-blog-building-experience', 'My First Blog\r\n=============\r\nI was wondering how to build a blog web application. Then I researched and researched a lot to get idea on how to build a good blog. After jotting down lot of things finally I came up with this.\r\n\r\nPersonal Blog\r\n=============\r\nThe idea of personal blog was not my first one, first I thought of something like Android application or a good social website, but those are far reality for me as I didn''t have the enough knowledge of those. Then I started a course in Udacity on Web Development. I got some very important knowledge and acquired some relevant skills regarding web development. Finally, I came up with a idea why not develop this blog using Django as Python is my primary language and Django is a hot topic for Python developers. When I started this project I faced some problems how to get started in Django, but thank god! there is lot of tutorials available online to get started on Django.\r\n\r\nWorking With Django\r\n===================\r\nI got a basic tutorial on Django from Udemy then after a lot of search I got [GettingStartedWithDjango](http://gettingstartedwithdjango.com/ "") tutorial which is very good to start a Django project from development to production. It taught me how to setup a Django development server and Google also help me to find a blog post where I got how to setup my production server on AWS EC2 [[link](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/ "")].\r\n\r\n<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-in.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=IN&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=rohanroycom-21&marketplace=amazon&region=IN&placement=B00KR9NT5C&asins=B00KR9NT5C&linkId=&show_border=true&link_opens_in_new_window=true">\r\n', '', 1, 'p', ''),
(3, '2015-04-20 16:39:17', '2016-07-26 11:43:50', 'my experience in capgemini', 'my-experience-capgemini', 'Today in this post I''m going to share my experience in Capgemini. After completing my graduation I joined Capgemini as a Software Engineer. Today I gonna share how I got into Capgemini and how its changed my life.\r\n\r\n**Campus Placement**\r\n\r\nFor everyone getting placed into a MNC is a dream but for me it was a challenge. Because by then I wasn''t ready for corporate life though I needed a job to get the taste of my own money :) . Here comes my story of getting placed in Capgemini. After getting rejected from TCS, who came first on our college I was hopping that I would get placed into our next visitor. Fortunately our next visitor was Capgemini but unfortunately I was late for the first round (Aptitude Round) of their selection process. Actually I always come out late on my important life events, so it was not a coincidence. But I somehow managed to convince our TPO (Training & Placement Officer) to arrange a test for me and he did this for me. When the result declared I found I was selected for the next round and that was Group Discussion Round. Again this time I was late as I hadn''t any formal dress with me right then so I had to borrow it from one my friend. It was a good round for me and I was selected for the Personal Interview Round.\r\n\r\n**Personal Interview**\r\n\r\nHonestly, I was so nervous for my personal interview but I didn''t show it to anyone. Everyone of my friends was thinking that it was just like a piece of cake for me, I would definitely crack it. But only I knew that what was the actual situation inside myself. It was like sailing a ship in the storm. But when I got into the room I had a believe that they came here to pick the best talent and I need to show them what they want. The interviewer asked me some questions on my field and I replied with confidence. After the interview, I knew that I gave my best shot. Finally, after an hour of discussion they came up with the job offer and guess what I found myself on that offer list. I was excited, thrilled and blast out my every bit of emotion in enjoyment. So this was my exciting story of getting placed into Capgemini.\r\n\r\n**In Capgemini**\r\n\r\nI thing the journey with Capgemini was more exciting than getting into it. For few days after my joining it was really hard time for me as I need to wake up early in the morning to attend the training sessions. We were trained on SAP ABAP, I think you didn''t get it, actually me neither on my first time when I heard SAP. Even I didn''t know how to pronounce it correctly. Actually it is pronounced as its syllable itself (''S'', ''A'', ''P''). Except training on SAP ABAP Capgemini gave me lot of things like it gave me some good friends with whom I can chill out my nights, watch movies or visit a nearby place to enjoy the evening and lot of things for that I need dare to put here ;) . \r\n\r\n<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-in.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=IN&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=rohanroycom-21&marketplace=amazon&region=IN&placement=B00YSBTLWA&asins=B00YSBTLWA&show_border=true&link_opens_in_new_window=true&linkId=">\r\n</iframe>\r\n\r\n', '', 1, 'd', ''),
(4, '2016-02-02 11:23:00', '2016-08-08 15:01:56', 'Movie Task Documentation', 'movie-task-documentation', '# [Movie Task][2]\r\n----------------\r\n\r\n Movie Task app is an implementation for movie searching APIs. It is built with [Python][0] using the [Django Web Framework][1] and the APIs are implemented using [Django Rest Framework]. This app is deployed in [Heroku][3].\r\n\r\nThis project has the following basic apps:\r\n\r\n* API -- This app handles all the API requests and responses\r\n* Movie -- This app represents all the Movie and Genre models\r\n* Account -- This app handles the user logins and registrations\r\n* Profile -- This app is for personalizing the user profile\r\n\r\n## Installation\r\n\r\n### Quick start\r\n\r\nTo set up a development environment quickly, first install Python 3. It\r\ncomes with virtualenv built-in. So create a virtual env by:\r\n\r\n1. `$ python3 -m venv movie_task`\r\n2. `$ . movie_task/bin/activate`\r\n\r\nInstall all dependencies:\r\n\r\npip install -r requirements.txt\r\n\r\nRun migrations:\r\n\r\npython manage.py migrate\r\n\r\n### Detailed instructions\r\n\r\nTake a look at the docs for more information.\r\n\r\n\r\nAPI Documentation\r\n------------------------\r\nThis is Fynd Movie Task API resource documatation. To test the APIs use these demo users\r\n\r\nusername\r\n\r\nThe API provides endpoints for movies and users. It can be accessed via a simple API call.\r\n\r\nThe API defines the following endpoints:\r\n\r\n> * https://movie-task.herokuapp.com/users/\r\n> * https://movie-task.herokuapp.com/movies/\r\n\r\nIn case of a successful users request like,\r\n\r\n> * https://movie-task.herokuapp.com/api/users/1/\r\n\r\nthe JSON object returned looks like:\r\n\r\n    {\r\n    "url": "http://localhost:8000/api/users/1/"\r\n    "name": "Rohan",\r\n    "email": "b4you0870@gmail.com",\r\n    "movies": "http://localhost:8000/api/movies/1/" \r\n    }\r\n\r\nIn case of a successful movies request like,\r\n\r\n> https://movie-task.herokuapp.com/api/movies/1/\r\n\r\nthe JSON object returned looks like,\r\n\r\n    {\r\n    "url": "http://movie-task.herokuapp.com/api/movies/1/",\r\n    "name": "Toy Story",\r\n    "director": "John Lasseter",\r\n    "genres": [\r\n	    "Adventure",\r\n	    "Comedy",\r\n	    "Animation"\r\n    ],\r\n    "release": "1991-11-19",\r\n    "imdb_score": 8.3,\r\n    "popularity": 92,\r\n    "owner": "b4you0870@gmail.com"\r\n    }\r\n\r\nIf an unauthenticated / Anonymous user tries to create a Movie instance the following response will be generated\r\n\r\n    HTTP 403 Forbidden\r\n    Content-Type: application/json\r\n    Vary: Accept\r\n    Allow: GET, POST, HEAD, OPTIONS\r\n    \r\n    {\r\n        "detail": "Permission denied."\r\n    }\r\n\r\nFilter can be applied on the following parameters:\r\n\r\n> **`name`** -- `https://movie-task.herokuapp.com/api/movies/?name="Toy Story"`\r\n> \r\n> **`director`** --`https://movie-task.herokuapp.com/api/movies/?director=''John Lasseter''`\r\n> \r\n> **`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation`\r\n> \r\n> or\r\n> For multiple filter on Genre elements\r\n> **`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation,Comedy`\r\n> \r\n> **`min_imdb`** -- `https://movie-task.herokuapp.com/api/movies/?min_imdb=8`\r\n> \r\n> **`max_imdb`** -- `https://movie-task.herokuapp.com/api/movies/?max_imdb=8`\r\n\r\n[0]: https://www.python.org/\r\n[1]: https://www.djangoproject.com/\r\n[2]: https://movie-task.herokuapp.com/\r\n[3]: https://www.heroku.com/)(http://www.django-rest-framework.org/\r\n<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-in.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=IN&source=ac&ref=qf_sp_asin_til&ad_type=product_link&tracking_id=rohanroycom-21&marketplace=amazon&region=IN&placement=B01FKEB2SE&asins=B01FKEB2SE&linkId=&show_border=true&link_opens_in_new_window=true">\r\n</iframe>\r\n\r\n<a href="https://www.amazon.in/OnePlus-3-Graphite-64GB/dp/B01DDP7UQ0/ref=as_li_ss_il?ie=UTF8&ref_=as_li_ss_tl&ref_=cm_sw_r_wa_api_i_dZjQxbMB5895S&linkCode=li2&tag=rohanroycom-21&linkId=7421228c8076d1da9a0e8ec778d9b548" target="_blank"><img border="0" src="//ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01DDP7UQ0&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=rohanroycom-21" ></a><img src="https://ir-in.amazon-adsystem.com/e/ir?t=rohanroycom-21&l=li2&o=31&a=B01DDP7UQ0" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />', '', 1, 'p', '');

-- --------------------------------------------------------

--
-- Table structure for table `blog_post_tags`
--

CREATE TABLE IF NOT EXISTS `blog_post_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `post_id` (`post_id`,`tag_id`),
  KEY `blog_post_tags_f3aa1999` (`post_id`),
  KEY `blog_post_tags_76f094bc` (`tag_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=135 ;

--
-- Dumping data for table `blog_post_tags`
--

INSERT INTO `blog_post_tags` (`id`, `post_id`, `tag_id`) VALUES
(125, 1, 1),
(111, 2, 1),
(112, 2, 2),
(113, 2, 3),
(114, 2, 4),
(115, 2, 5),
(126, 3, 2),
(127, 3, 3),
(128, 3, 6),
(129, 3, 7),
(130, 3, 8),
(131, 3, 9),
(132, 4, 1),
(134, 4, 4),
(133, 4, 12);

-- --------------------------------------------------------

--
-- Table structure for table `blog_privacy`
--

CREATE TABLE IF NOT EXISTS `blog_privacy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `appname` varchar(30) NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `blog_privacy`
--

INSERT INTO `blog_privacy` (`id`, `appname`, `content`) VALUES
(1, 'Vorec', '**Privacy Policy**\r\n==================\r\nIn order to receive information about your Personal Data, the purposes and the parties the Data is shared with, contact the Owner.\r\n\r\n**Data Controller and Owner**\r\n-------------------------\r\n\r\nTypes of Data collected\r\n-----------------------\r\nThe owner does not provide a list of Personal Data types collected.\r\nOther Personal Data collected may be described in other sections of this privacy policy or by dedicated explanation text contextually with the Data collection.\r\nThe Personal Data may be freely provided by the User, or collected automatically when using this Application.\r\nAny use of Cookies - or of other tracking tools - by this Application or by the owners of third party services used by this Application, unless stated otherwise, serves to identify Users and remember their preferences, for the sole purpose of providing the service required by the User.\r\nFailure to provide certain Personal Data may make it impossible for this Application to provide its services.\r\nUsers are responsible for any Personal Data of third parties obtained, published or shared through this Application and confirm that they have the third party''s consent to provide the Data to the Owner.\r\n\r\nMode and place of processing the Data\r\n-------------------------------------\r\nMethods of processing\r\n---------------------\r\nThe Data Controller processes the Data of Users in a proper manner and shall take appropriate security measures to prevent unauthorised access, disclosure, modification, or unauthorised destruction of the Data.\r\nThe Data processing is carried out using computers and/or IT enabled tools, following organisational procedures and modes strictly related to the purposes indicated. In addition to the Data Controller, in some cases, the Data may be accessible to certain types of persons in charge, involved with the operation of the site (administration, sales, marketing, legal, system administration) or external parties (such as third party technical service providers, mail carriers, hosting providers, IT companies, communications agencies) appointed, if necessary, as Data Processors by the Owner. The updated list of these parties may be requested from the Data Controller at any time.\r\n\r\nPlace\r\n-----\r\nThe Data is processed at the Data Controller''s operating offices and in any other places where the parties involved with the processing are located. For further information, please contact the Data Controller.\r\n\r\nRetention time\r\n--------------\r\nThe Data is kept for the time necessary to provide the service requested by the User, or stated by the purposes outlined in this document, and the User can always request that the Data Controller suspend or remove the data.\r\n\r\n**Additional information about Data collection and processing**\r\n-----------------------------------------------------------\r\nLegal action\r\n------------\r\nThe User''s Personal Data may be used for legal purposes by the Data Controller, in Court or in the stages leading to possible legal action arising from improper use of this Application or the related services.\r\nThe User declares to be aware that the Data Controller may be required to reveal personal data upon request of public authorities.\r\n\r\n**Additional information about User''s Personal Data**\r\n-------------------------------------------------\r\nIn addition to the information contained in this privacy policy, this Application may provide the User with additional and contextual information concerning particular services or the collection and processing of Personal Data upon request.\r\n\r\nSystem logs and maintenance\r\n---------------------------\r\nFor operation and maintenance purposes, this Application and any third party services may collect files that record interaction with this Application (System logs) or use for this purpose other Personal Data (such as IP Address).\r\n\r\nInformation not contained in this policy\r\n----------------------------------------\r\nMore details concerning the collection or processing of Personal Data may be requested from the Data Controller at any time. Please see the contact information at the beginning of this document.\r\n\r\nThe rights of Users\r\n----------------------------------------\r\n\r\nUsers have the right, at any time, to know whether their Personal Data has been stored and can consult the Data Controller to learn about their contents and origin, to verify their accuracy or to ask for them to be supplemented, cancelled, updated or corrected, or for their transformation into anonymous format or to block any data held in violation of the law, as well as to oppose their treatment for any and all legitimate reasons. Requests should be sent to the Data Controller at the contact information set out above.\r\nThis Application does not support “Do Not Track” requests.\r\nTo determine whether any of the third party services it uses honour the “Do Not Track” requests, please read their privacy policies.\r\n\r\nChanges to this privacy policy\r\n----------------------------------------\r\n\r\nThe Data Controller reserves the right to make changes to this privacy policy at any time by giving notice to its Users on this page. It is strongly recommended to check this page often, referring to the date of the last modification listed at the bottom. If a User objects to any of the changes to the Policy, the User must cease using this Application and can request that the Data Controller remove the Personal Data. Unless stated otherwise, the then-current privacy policy applies to all Personal Data the Data Controller has about Users.\r\n\r\nInformation about this privacy policy\r\n----------------------------------------\r\n\r\nThe Data Controller is responsible for this privacy policy, prepared starting from the modules provided by Rohan Roy and hosted on http://rohanroy.com servers.\r\n\r\n**Definitions and legal references**\r\n----------------------------------------\r\n\r\n\r\nPersonal Data (or Data)\r\n----------------------------------------\r\n\r\nAny information regarding a natural person, a legal person, an institution or an association, which is, or can be, identified, even indirectly, by reference to any other information, including a personal identification number.\r\n\r\nUsage Data\r\n----------------------------------------\r\n\r\nInformation collected automatically from this Application (or third party services employed in this Application), which can include: the IP addresses or domain names of the computers utilised by the Users who use this Application, the URI addresses (Uniform Resource Identifier), the time of the request, the method utilised to submit the request to the server, the size of the file received in response, the numerical code indicating the status of the server''s answer (successful outcome, error, etc.), the country of origin, the features of the browser and the operating system utilised by the User, the various time details per visit (e.g., the time spent on each page within the Application) and the details about the path followed within the Application with special reference to the sequence of pages visited, and other parameters about the device operating system and/or the User''s IT environment.\r\n\r\nUser\r\n----------------------------------------\r\n\r\nThe individual using this Application, which must coincide with or be authorised by the Data Subject, to whom the Personal Data refers.\r\n\r\nData Subject\r\n----------------------------------------\r\n\r\nThe legal or natural person to whom the Personal Data refers.\r\n\r\nData Processor (or Data Supervisor)\r\n----------------------------------------\r\n\r\nThe natural person, legal person, public administration or any other body, association or organisation authorised by the Data Controller to process the Personal Data in compliance with this privacy policy.\r\n\r\nData Controller (or Owner)\r\n----------------------------------------\r\n\r\nThe natural person, legal person, public administration or any other body, association or organisation with the right, also jointly with another Data Controller, to make decisions regarding the purposes, and the methods of processing of Personal Data and the means used, including the security measures concerning the operation and use of this Application. The Data Controller, unless otherwise specified, is the Owner of this Application.\r\n\r\nThis Application\r\n----------------------------------------\r\n\r\nThe hardware or software tool by which the Personal Data of the User is collected.\r\n\r\nLegal information\r\n----------------------------------------\r\n\r\nNotice to European Users: this privacy statement has been prepared in fulfilment of the obligations under Art. 10 of EC Directive n. 95/46/EC, and under the provisions of Directive 2002/58/EC, as revised by Directive 2009/136/EC, on the subject of Cookies.\r\n\r\n_This privacy policy relates solely to this Application._');

-- --------------------------------------------------------

--
-- Table structure for table `blog_project`
--

CREATE TABLE IF NOT EXISTS `blog_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `date` date NOT NULL,
  `slug` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `github` varchar(255) NOT NULL,
  `subtitle` varchar(255) DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  `side_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `blog_project`
--

INSERT INTO `blog_project` (`id`, `title`, `content`, `image`, `date`, `slug`, `url`, `github`, `subtitle`, `status`, `side_image`) VALUES
(1, 'Weather- Designed for Android', 'Its a weather app for Android which fetches hourly weather data from weather.com. I used Android Studio to create this app and used JSON to parse the weather API.', 'projectlist/projects/1463337103-98c58555-3ca1-4779-ad83-9c08220b7fae.png', '2014-04-20', 'weather-designed-android', 'https://www.udacity.com/course/ud853', 'https://github.com/triump0870/weather', 'Android App', 'p', 'projects/side/1463905925-f4eb0077-4e44-4b8a-88ee-4172604e1db3.png'),
(2, 'Gamazone- Developed for Gamers', 'Its a website for gamers to share there experience on Video games and help others to overcome the problems they faced while they were playing.', 'projectlist/projects/1434104857-2933b86b-0162-4c9a-9a1e-22e424e18ce5.jpg', '2014-03-21', 'gamazone-developed-gamers', 'https://github.com/triump0870/gamazone', 'https://github.com/triump0870/gamazone', '', 'p', 'projects/side/1463906774-80fe3e9e-3e13-4e45-a2f1-ebb1d2d1abed.png'),
(3, 'Interactive Games - Designed on Codeskulptor using Python', 'I developed several browser based games on codeskulptor while taking a course in coursera on An Introduction to Interactive Programming in Python under Joe Warren, Scott Rixner, John Greiner & Stephen Wong of Rice University. Amongst my all games the most notable one is [Galaxy Invaders](http://www.codeskulptor.org/#user23_fTVPDKIDhRdCfUp.py "Galaxy Invaders")', 'projectlist/projects/1434108692-4749e7c5-7b34-4ca3-a327-333e57add304.jpg', '2013-11-20', 'interactive-games-designed-codeskulptor-using-python', 'https://www.coursera.org/course/interactivepython', 'https://github.com/triump0870/Interactive_Programming_Python', '', 'p', 'projects/side/1463907553-8747c752-a308-4c6a-b76d-b89d2f4c1419.png'),
(4, 'Bitstarter- Startup Engineering', 'I took a course on Coursera on Startup Engineering under Balaji S. Srinivasan & Vijay S. Pande of Standford University. Here I learned a fast-paced introduction to key tools and techniques like command line, dotfiles, text editor, distributed version control, debugging, testing, documentation, reading code, deployments etc. For the project I developed a web server on AWS EC2 and hosted a static website using Heroku.', 'projectlist/projects/1434109994-19c05aec-8621-430e-b05c-6f348773b568.jpg', '2013-11-07', 'bitstarter-startup-engineering', 'https://www.coursera.org/course/startup', 'https://github.com/triump0870/bitstarter', '', 'p', 'projects/side/1463907656-5af02227-4740-418b-b9c2-c7cbaaa8982f.png'),
(5, 'KickStarter - Miniblog', 'This is my Personal Blog Project which is developed in Django1.7. The website is hosted in an AWS Linux instance under Nginx server. I used Virtualenv to make an isolated Django environment. Here I used Gunicorn to wrap the Django environment as Django is single threaded so it is incapable of handling multiple simultaneous requests where Gunicorn server can serve several simultaneous request at the same time. I used Nginx to serve the static files as Gunicorn is incapable of serving static files. Again the Gunicorn server is supervised by the Supervisor so that when it gets stopped or killed abruptly, Supervisor will start it automatically so that website is always keep running.\r\n\r\nI am new to Django so if you have any suggestion or interested to contribute then you are always welcome to contribute in this project to make your experience better.\r\n', 'projectlist/projects/1463899690-ecb0b3d7-9cb3-40a7-95d0-cc6f6bcac4bd.jpg', '2014-12-20', 'kickstarter-miniblog', 'http://rohanroy.com/', 'https://github.com/triump0870/miniblog', 'A simple Personal blog', 'p', 'projects/side/1463899690-454938e5-0a4d-44f6-903c-0bf696cd9f74.png'),
(6, 'Vamrine', 'Vamrine helps you to organise your everyday tasks with interactive interactions. We used voice recognition technique, so you can set your task over voice commands. You can specify the time of task execution and Vamrine will let you know when you need to get started through a voice alarm. If you forget to complete the task you will get motivating notification both text based and voice based, so that you find the right energy to get back into the task.', 'projectlist/projects/1463905484-3bc84ab7-6199-4d97-b4cd-1a8c8e395242.png', '2016-05-22', 'vamrine', 'http://com.rohanroy.vamrine', 'https://github.com/triump0870/vamrine', 'A Task Management App', 'p', 'projects/side/1463904968-06b9e820-ddeb-4a15-b097-89cb2bc70ca3.png'),
(7, 'Vorec', 'The Vorec App is an app that records a message and plays the audio back through user-selected filters. \r\n\r\nIt allows users to record a sound using the device’s microphone. It then allows users to play the recorded sound back with six different sound modulations: Snail, Rabbit, Chipmunk, Darth Vader, Echo and Reverb.\r\n', 'projectlist/projects/1469561905-52fcd57d-5f39-4289-8fb6-10d266aad1af.png', '2016-07-27', 'vorec', '', 'https://github.com/triump0870/vorec', 'Dubsmash for audio ', 'p', 'projects/side/1469562003-fdcd63d2-63e1-4538-a205-73329da1e6b7.png');

-- --------------------------------------------------------

--
-- Table structure for table `blog_skill`
--

CREATE TABLE IF NOT EXISTS `blog_skill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `stage` varchar(15) NOT NULL,
  `rating` int(11) NOT NULL,
  `info` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `blog_skill`
--

INSERT INTO `blog_skill` (`id`, `name`, `stage`, `rating`, `info`) VALUES
(1, 'Python', 'Proficient', 75, 'I can find and fix your bugs.'),
(2, 'Django & Django REST', 'Proficient', 70, 'I can build a webpage from scratch.'),
(3, 'Mysql & Git', 'Proficient', 60, 'I can make you understand what I''m doing.'),
(4, 'iOS & Swift', 'Beginner', 55, 'Right now I''m learning.');

-- --------------------------------------------------------

--
-- Table structure for table `blog_tag`
--

CREATE TABLE IF NOT EXISTS `blog_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `blog_tag`
--

INSERT INTO `blog_tag` (`id`, `slug`) VALUES
(10, 'adventure'),
(2, 'Blog'),
(6, 'Campusing'),
(8, 'Capgemini'),
(7, 'college'),
(1, 'Django'),
(12, 'documentation'),
(9, 'Job'),
(5, 'Linux'),
(4, 'Python'),
(11, 'travel'),
(3, 'Writing');

-- --------------------------------------------------------

--
-- Table structure for table `blog_userdata`
--

CREATE TABLE IF NOT EXISTS `blog_userdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `user` varchar(70) NOT NULL,
  `role` varchar(30) NOT NULL,
  `location` varchar(100) NOT NULL,
  `contact` varchar(70) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `linkedin` varchar(200) DEFAULT NULL,
  `facebook` varchar(200) DEFAULT NULL,
  `twitter` varchar(200) DEFAULT NULL,
  `googleplus` varchar(200) DEFAULT NULL,
  `github` varchar(200) DEFAULT NULL,
  `hackernews` varchar(200) DEFAULT NULL,
  `email` varchar(70) NOT NULL,
  `testimonial` longtext NOT NULL,
  `testimonial_name` varchar(255) NOT NULL,
  `testimonial_desig` varchar(70) NOT NULL,
  `testimonial_link` varchar(200) DEFAULT NULL,
  `border_color` varchar(10) DEFAULT NULL,
  `border_width` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `blog_userdata`
--

INSERT INTO `blog_userdata` (`id`, `fullname`, `user`, `role`, `location`, `contact`, `website`, `linkedin`, `facebook`, `twitter`, `googleplus`, `github`, `hackernews`, `email`, `testimonial`, `testimonial_name`, `testimonial_desig`, `testimonial_link`, `border_color`, `border_width`, `image`) VALUES
(1, 'Rohan Roy', 'triump0870', 'Web Developer', 'Bangalore, IN', 'rohan@rohanroy.com', 'http://rohanroy.com/', 'https://linkedin.com/in/triump0870', 'https://facebook.com/triump0870', 'https://twitter.com/triump0870', 'https://plus.google.com/+RohanRoy1', 'https://github.com/triump0870', 'https://news.ycombinator.com/user?id=triump0870', 'b4you0870@gmail.com', 'Rohan is an excellent software engineer and he is passionate about what he does. You can totally count on him to deliver your projects!', 'Tamal Biswas', 'Software Engineer', 'https://www.linkedin.com/profile/view?id=316739437', 'ADC7F0', 5, 'avater/1444232360-9e3e3084-d8fe-4e17-b930-f493fb312607.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `blog_work`
--

CREATE TABLE IF NOT EXISTS `blog_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(255) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `content` longtext NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `website` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `blog_work`
--

INSERT INTO `blog_work` (`id`, `company`, `designation`, `content`, `start_date`, `end_date`, `website`) VALUES
(1, 'Nettech', 'Trainee', 'I did winter training on Network Management at a company named Nettech. There I learned to apply my knowledge of computer networks. Nettech is a computer networking training provider headquartered in Kolkata, India. Its courses focus on computer networking in the Linux environment, network security, information security management systems and counter measures against hacking and other cybercrimes .', '2012-12-20', '2013-01-10', 'http://www.nettech.in/'),
(3, 'Ericsson', 'Integration Engineer', '* Developed initial phase of trip planning app(EriTrip).\r\n- Developed RESTful API endpoints using Django-Rest Framework and\r\nMySQL database to integrate Meeting Room booking app (Confrentu) with the\r\nEricsson Intranet.', '2014-07-23', '2015-10-26', 'http://ericsson.com/'),
(4, 'HackerEarth', 'Software Developer', '* Designed REST APIs that allows sophisticated, effective and low-cost application integration.\r\n* Implemented designs, including experimentation and multiple iterations.\r\n* Collaborate with other team members to plan, design and develop robust solutions.\r\n', '2015-11-02', NULL, 'https://hackerearth.com/');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=196 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2015-04-16 09:50:02', '1', 'Django', 1, '', 7, 1),
(2, '2015-04-16 09:52:40', '1', 'my first django app', 1, '', 8, 1),
(3, '2015-04-19 12:26:30', '2', 'Blog', 1, '', 7, 1),
(4, '2015-04-19 12:26:43', '3', 'Writing', 1, '', 7, 1),
(5, '2015-04-19 12:26:55', '4', 'Python', 1, '', 7, 1),
(6, '2015-04-19 12:27:07', '5', 'Linux', 1, '', 7, 1),
(7, '2015-04-19 12:27:13', '2', 'My First Blog Writing Experience', 1, '', 8, 1),
(8, '2015-04-19 21:22:06', '2', 'My First Blog Writing Experience', 2, 'Changed content.', 8, 1),
(9, '2015-04-19 21:24:12', '2', 'My First Blog Writing Experience', 2, 'Changed content.', 8, 1),
(10, '2015-04-19 21:26:15', '2', 'My First Blog Writing Experience', 2, 'Changed content.', 8, 1),
(11, '2015-04-19 21:28:55', '2', 'My First Blog Writing Experience', 2, 'Changed content.', 8, 1),
(12, '2015-04-20 14:48:54', '1', 'Weather- Designed for Android', 1, '', 11, 1),
(13, '2015-04-20 14:49:44', '2', 'Gamazone- Developed for Gamers', 1, '', 11, 1),
(14, '2015-04-20 14:50:35', '3', 'Interactive Games - Designed on Codeskulptor using Python', 1, '', 11, 1),
(15, '2015-04-20 14:52:05', '4', 'Bitstarter- Startup Engineering', 1, '', 11, 1),
(16, '2015-04-20 14:52:48', '5', 'KickStarter - Miniblog', 1, '', 11, 1),
(17, '2015-04-20 15:36:22', '1', 'Internship', 1, '', 12, 1),
(18, '2015-04-20 15:36:43', '2', 'Software Engineer', 1, '', 12, 1),
(19, '2015-04-20 15:37:00', '3', 'Integration Engineer', 1, '', 12, 1),
(20, '2015-04-20 16:39:17', '3', 'my experience in capgemini', 1, '', 8, 1),
(21, '2015-04-20 17:57:23', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(22, '2015-04-20 19:26:18', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(23, '2015-04-20 19:28:14', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(24, '2015-04-20 19:59:08', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(25, '2015-04-20 19:59:30', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(26, '2015-04-20 20:01:44', '6', 'Campusing', 1, '', 7, 1),
(27, '2015-04-20 20:01:54', '7', 'college', 1, '', 7, 1),
(28, '2015-04-20 20:02:03', '8', 'Capgemini', 1, '', 7, 1),
(29, '2015-04-20 20:02:40', '9', 'Job', 1, '', 7, 1),
(30, '2015-04-20 20:02:46', '3', 'my experience in capgemini', 2, 'Changed content and tags.', 8, 1),
(31, '2015-04-21 19:20:41', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(32, '2015-04-21 19:21:38', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(33, '2015-04-21 19:23:34', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(34, '2015-04-21 19:24:29', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(35, '2015-04-21 19:26:29', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(36, '2015-04-21 19:29:29', '2', 'My Personal blog building experience', 2, 'Changed title and slug.', 8, 1),
(37, '2015-04-21 19:31:38', '2', 'My Personal blog building experience', 2, 'Changed content.', 8, 1),
(38, '2015-04-21 19:32:31', '2', 'My Personal blog building experience', 2, 'Changed content.', 8, 1),
(39, '2015-04-21 19:32:43', '2', 'My Personal blog building experience', 2, 'Changed content.', 8, 1),
(40, '2015-04-22 17:45:42', '1', 'example.com', 3, '', 13, 1),
(41, '2015-04-22 17:45:50', '2', 'rohanroy.com', 1, '', 13, 1),
(42, '2015-04-22 20:16:46', '1', 'About object', 1, '', 14, 1),
(43, '2015-04-22 20:16:53', '2', 'About object', 1, '', 14, 1),
(44, '2015-04-22 20:17:03', '3', 'About object', 1, '', 14, 1),
(45, '2015-04-22 20:52:55', '1', 'Python & Linux', 1, '', 15, 1),
(46, '2015-04-22 20:53:07', '2', 'HTML & CSS', 1, '', 15, 1),
(47, '2015-04-22 20:53:27', '3', 'Algorithms, Mysql & Git', 1, '', 15, 1),
(48, '2015-04-22 20:53:40', '4', 'Django, Bootstrap & JS', 1, '', 15, 1),
(49, '2015-04-22 20:54:35', '2', 'HTML & CSS', 2, 'Changed stage and rating.', 15, 1),
(50, '2015-04-22 20:55:01', '1', 'Python & Linux', 2, 'Changed stage and rating.', 15, 1),
(51, '2015-04-22 21:36:09', '1', 'Computer Science', 1, '', 16, 1),
(52, '2015-04-22 21:36:27', '2', 'Web Development', 1, '', 16, 1),
(53, '2015-04-22 21:52:15', '3', 'Full Stack Web Developer', 1, '', 16, 1),
(54, '2015-04-22 21:52:45', '3', 'Full Stack Developer', 2, 'Changed course.', 16, 1),
(55, '2015-04-23 08:40:40', '1', 'Trainee', 2, 'Changed designation.', 12, 1),
(56, '2015-04-23 08:41:47', '1', 'Trainee', 2, 'Changed content.', 12, 1),
(57, '2015-04-23 08:43:23', '2', 'Software Engineer', 2, 'Changed content.', 12, 1),
(58, '2015-04-23 08:47:02', '2', 'Software Engineer', 2, 'Changed content.', 12, 1),
(59, '2015-04-23 09:09:16', '1', 'We Code Hard', 1, '', 17, 1),
(60, '2015-04-23 09:09:31', '2', 'Until The Morning', 1, '', 17, 1),
(61, '2015-04-23 09:11:36', '3', 'Muse - Uprising', 1, '', 17, 1),
(62, '2015-04-23 09:12:12', '4', 'End Of Line', 1, '', 17, 1),
(63, '2015-04-23 09:15:31', '3', 'Integration Engineer', 2, 'Changed content.', 12, 1),
(64, '2015-04-23 09:56:20', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(65, '2015-04-23 11:35:44', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(66, '2015-04-24 09:44:15', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(67, '2015-04-24 09:55:08', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(68, '2015-04-24 17:25:03', '1', 'triump0870', 1, '', 18, 1),
(69, '2015-04-24 17:28:23', '5', 'KickStarter - Miniblog', 2, 'Changed subtitle.', 11, 1),
(70, '2015-04-24 17:28:49', '1', 'Bengali', 1, '', 19, 1),
(71, '2015-04-24 17:28:59', '2', 'English', 1, '', 19, 1),
(72, '2015-04-24 17:29:19', '3', 'Hindi', 1, '', 19, 1),
(73, '2015-04-24 17:45:38', '1', 'TCS Code Vita', 1, '', 20, 1),
(74, '2015-04-24 17:46:31', '2', 'DGPLug Summer Training', 1, '', 20, 1),
(75, '2015-04-24 18:04:07', '3', 'Integration Engineer', 2, 'Changed website.', 12, 1),
(76, '2015-04-24 18:06:47', '2', 'Software Engineer', 2, 'Changed website.', 12, 1),
(77, '2015-04-24 18:08:16', '1', 'Trainee', 2, 'Changed website.', 12, 1),
(78, '2015-04-24 18:09:42', '1', 'Trainee', 2, 'No fields changed.', 12, 1),
(79, '2015-04-24 18:09:43', '1', 'Trainee', 2, 'No fields changed.', 12, 1),
(80, '2015-04-24 18:18:08', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(81, '2015-04-24 18:19:08', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(82, '2015-04-24 18:19:56', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(83, '2015-04-24 18:20:21', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(84, '2015-04-24 18:20:49', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(85, '2015-04-24 18:21:37', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(86, '2015-04-25 04:40:36', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(87, '2015-04-25 04:42:07', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(88, '2015-04-25 04:43:56', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(89, '2015-04-25 04:52:00', '1', 'Weather- Designed for Android', 2, 'Changed image.', 11, 1),
(90, '2015-04-25 04:54:46', '1', 'Weather- Designed for Android', 2, 'Changed date and subtitle.', 11, 1),
(91, '2015-04-28 09:22:31', '2', 'avishek', 1, '', 4, 1),
(92, '2015-04-28 09:25:48', '2', 'avishek', 2, 'Changed first_name, last_name, email and user_permissions.', 4, 1),
(93, '2015-05-07 19:59:39', '2', 'avishek', 2, 'Changed password.', 4, 1),
(94, '2015-05-07 20:00:46', '2', 'avishek', 2, 'Changed password.', 4, 1),
(95, '2015-05-09 09:09:27', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(96, '2015-05-09 09:10:33', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(97, '2015-05-10 13:54:37', '10', 'adventure', 1, '', 7, 1),
(98, '2015-05-10 13:55:39', '11', 'travel', 1, '', 7, 1),
(99, '2015-05-14 19:44:52', '1', 'About object', 2, 'Changed content.', 14, 1),
(100, '2015-05-15 20:02:56', '1', 'triump0870', 2, 'Changed image, border_color and border_width.', 18, 1),
(101, '2015-05-15 20:04:21', '4', 'Django, Bootstrap & JS', 2, 'Changed info.', 15, 1),
(102, '2015-05-15 20:04:42', '3', 'Algorithms, Mysql & Git', 2, 'Changed info.', 15, 1),
(103, '2015-05-15 20:05:06', '2', 'HTML & CSS', 2, 'Changed info.', 15, 1),
(104, '2015-05-15 20:05:25', '1', 'Python & Linux', 2, 'Changed info.', 15, 1),
(105, '2015-05-25 10:08:06', '4', 'Django, Bootstrap & JS', 2, 'No fields changed.', 15, 1),
(106, '2015-05-25 10:08:30', '1', 'Python & Linux', 2, 'Changed stage.', 15, 1),
(107, '2015-05-25 10:08:38', '2', 'HTML & CSS', 2, 'Changed stage.', 15, 1),
(108, '2015-05-25 10:08:45', '3', 'Algorithms, Mysql & Git', 2, 'Changed stage.', 15, 1),
(109, '2015-05-25 10:09:40', '4', 'Django, Bootstrap & JS', 2, 'Changed info.', 15, 1),
(110, '2015-05-25 10:17:11', '6', 'CourseStack', 1, '', 11, 1),
(111, '2015-05-28 12:57:37', '6', 'CourseStack', 2, 'Changed status.', 11, 1),
(112, '2015-05-28 13:03:15', '6', 'CourseStack', 2, 'Changed status.', 11, 1),
(113, '2015-05-28 13:03:35', '6', 'CourseStack', 3, '', 11, 1),
(114, '2015-06-10 11:39:38', '5', 'KickStarter - Miniblog', 2, 'Changed image and side_image.', 11, 1),
(115, '2015-06-10 11:43:00', '4', 'Bitstarter- Startup Engineering', 2, 'Changed image and side_image.', 11, 1),
(116, '2015-06-10 11:48:33', '3', 'Interactive Games - Designed on Codeskulptor using Python', 2, 'Changed image and side_image.', 11, 1),
(117, '2015-06-10 11:54:51', '2', 'Gamazone- Developed for Gamers', 2, 'Changed image and side_image.', 11, 1),
(118, '2015-06-10 11:59:50', '1', 'Weather- Designed for Android', 2, 'Changed image and side_image.', 11, 1),
(119, '2015-06-10 12:58:30', '1', 'Weather- Designed for Android', 2, 'Changed side_image.', 11, 1),
(120, '2015-06-11 09:59:07', '1', '1', 1, '', 22, 1),
(121, '2015-06-12 10:27:37', '2', 'Gamazone- Developed for Gamers', 2, 'Changed image.', 11, 1),
(122, '2015-06-12 11:23:19', '3', 'Interactive Games - Designed on Codeskulptor using Python', 2, 'Changed image.', 11, 1),
(123, '2015-06-12 11:24:36', '1', 'Weather- Designed for Android', 2, 'Changed image.', 11, 1),
(124, '2015-06-12 11:26:15', '1', 'Weather- Designed for Android', 2, 'Changed image.', 11, 1),
(125, '2015-06-12 11:27:46', '3', 'Interactive Games - Designed on Codeskulptor using Python', 2, 'Changed image.', 11, 1),
(126, '2015-06-12 11:31:32', '3', 'Interactive Games - Designed on Codeskulptor using Python', 2, 'Changed image and side_image.', 11, 1),
(127, '2015-06-12 11:50:32', '4', 'Bitstarter- Startup Engineering', 2, 'Changed image.', 11, 1),
(128, '2015-06-12 11:51:55', '4', 'Bitstarter- Startup Engineering', 2, 'Changed image.', 11, 1),
(129, '2015-06-12 11:53:14', '4', 'Bitstarter- Startup Engineering', 2, 'Changed image.', 11, 1),
(130, '2015-10-07 15:39:07', '1', 'triump0870', 2, 'Changed image.', 18, 1),
(131, '2015-10-07 15:39:20', '1', 'triump0870', 2, 'Changed image.', 18, 1),
(132, '2016-01-28 13:20:47', '5', 'KickStarter - Miniblog', 2, 'Changed image and side_image.', 11, 1),
(133, '2016-02-02 11:22:53', '12', 'documentation', 1, '', 7, 1),
(134, '2016-02-02 11:23:00', '4', 'Movie Task Documentation', 1, '', 8, 1),
(135, '2016-02-14 19:25:56', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(136, '2016-02-15 09:32:30', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(137, '2016-02-16 11:35:24', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(138, '2016-02-16 11:43:31', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(139, '2016-02-21 06:55:25', '4', 'Software Developer', 1, '', 12, 1),
(140, '2016-02-21 06:55:59', '3', 'Integration Engineer', 2, 'Changed end_date.', 12, 1),
(141, '2016-02-21 06:56:38', '3', 'Integration Engineer', 2, 'Changed content.', 12, 1),
(142, '2016-02-21 06:59:35', '3', 'Integration Engineer', 2, 'Changed content.', 12, 1),
(143, '2016-02-27 14:03:51', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(144, '2016-03-11 12:15:42', '2', 'Software Engineer', 3, '', 12, 1),
(145, '2016-03-11 12:16:06', '3', 'Integration Engineer', 2, 'Changed start_date.', 12, 1),
(146, '2016-03-11 12:16:26', '3', 'Integration Engineer', 2, 'No fields changed.', 12, 1),
(147, '2016-03-19 10:04:24', '5', 'KickStarter - Miniblog', 2, 'Changed content.', 11, 1),
(148, '2016-05-15 18:31:44', '1', 'Weather- Designed for Android', 2, 'Changed image and side_image.', 11, 1),
(149, '2016-05-22 06:42:11', '1', 'triump0870', 2, 'Changed location.', 18, 1),
(150, '2016-05-22 06:48:11', '5', 'KickStarter - Miniblog', 2, 'Changed image and side_image.', 11, 1),
(151, '2016-05-22 08:16:08', '6', 'Vamrine', 1, '', 11, 1),
(152, '2016-05-22 08:24:45', '6', 'Vamrine', 2, 'Changed subtitle and image.', 11, 1),
(153, '2016-05-22 08:32:06', '1', 'Weather- Designed for Android', 2, 'Changed side_image.', 11, 1),
(154, '2016-05-22 08:46:15', '2', 'Gamazone- Developed for Gamers', 2, 'Changed side_image.', 11, 1),
(155, '2016-05-22 08:59:13', '3', 'Interactive Games - Designed on Codeskulptor using Python', 2, 'Changed side_image.', 11, 1),
(156, '2016-05-22 09:00:56', '4', 'Bitstarter- Startup Engineering', 2, 'Changed side_image.', 11, 1),
(157, '2016-05-22 12:39:23', '4', 'Bootstrap & JS', 2, 'Changed name and rating.', 15, 1),
(158, '2016-05-22 12:40:08', '1', 'Python & Django', 2, 'Changed name.', 15, 1),
(159, '2016-05-22 12:41:11', '4', 'Android', 2, 'Changed name.', 15, 1),
(160, '2016-05-22 12:41:49', '1', 'Python', 2, 'Changed name.', 15, 1),
(161, '2016-05-22 12:42:07', '3', 'Mysql & Git', 2, 'Changed name and rating.', 15, 1),
(162, '2016-05-22 12:42:18', '2', 'Django', 2, 'Changed name.', 15, 1),
(163, '2016-06-03 10:28:25', '3', 'Pycon India', 1, '', 20, 1),
(164, '2016-06-03 10:29:39', '3', 'Pycon India', 2, 'Changed link.', 20, 1),
(165, '2016-06-03 10:29:47', '2', 'DGPLug Summer Training', 2, 'Changed status.', 20, 1),
(166, '2016-06-03 10:29:53', '1', 'TCS Code Vita', 2, 'Changed status.', 20, 1),
(167, '2016-06-03 10:34:24', '3', 'Pycon India 2015', 2, 'Changed name.', 20, 1),
(168, '2016-06-03 10:34:56', '4', 'DjangoCon Europe 2016', 1, '', 20, 1),
(169, '2016-06-03 10:49:23', '3', 'Full Stack Developer', 2, 'Changed status and end_date.', 16, 1),
(170, '2016-06-03 10:49:54', '2', 'Web Development', 2, 'Changed status and end_date.', 16, 1),
(171, '2016-06-03 10:50:19', '1', 'Computer Science', 2, 'Changed status.', 16, 1),
(172, '2016-07-18 14:15:15', '1', 'Vorec', 1, '', 23, 1),
(173, '2016-07-19 18:58:52', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(174, '2016-07-19 20:05:33', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(175, '2016-07-19 20:07:16', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(176, '2016-07-19 20:38:17', '2', 'My Personal blog building experience', 2, 'Changed content.', 8, 1),
(177, '2016-07-19 20:39:17', '3', 'my experience in capgemini', 2, 'Changed content.', 8, 1),
(178, '2016-07-19 20:40:31', '4', 'Movie Task Documentation', 2, 'Changed content.', 8, 1),
(179, '2016-07-19 21:16:24', '1', 'my first django app', 2, 'Changed content.', 8, 1),
(180, '2016-07-25 15:07:55', '1', '1', 2, 'Changed content.', 14, 1),
(181, '2016-07-25 15:11:30', '4', 'iOS', 2, 'Changed name.', 15, 1),
(182, '2016-07-25 15:12:05', '2', 'Django & Django REST', 2, 'Changed name.', 15, 1),
(183, '2016-07-26 11:42:58', '3', 'Integration Engineer', 2, 'Changed content.', 12, 1),
(184, '2016-07-26 11:43:28', '4', 'Software Developer', 2, 'Changed content.', 12, 1),
(185, '2016-07-26 11:43:50', '3', 'my experience in capgemini', 2, 'Changed status.', 8, 1),
(186, '2016-07-26 11:45:18', '3', 'Integration Engineer', 2, 'Changed end_date.', 12, 1),
(187, '2016-07-26 11:45:38', '3', 'Integration Engineer', 2, 'Changed end_date.', 12, 1),
(188, '2016-07-26 11:46:20', '3', 'Integration Engineer', 2, 'Changed start_date and end_date.', 12, 1),
(189, '2016-07-26 19:38:25', '7', 'Vorec', 1, '', 11, 1),
(190, '2016-07-26 19:40:04', '7', 'Vorec', 2, 'Changed side_image.', 11, 1),
(191, '2016-07-27 13:12:29', '1', '1', 2, 'Changed content.', 14, 1),
(192, '2016-07-27 13:14:20', '1', '1', 2, 'Changed content.', 14, 1),
(193, '2016-07-27 13:14:54', '4', 'iOS $ Swift', 2, 'Changed name.', 15, 1),
(194, '2016-07-27 13:15:01', '4', 'iOS & Swift', 2, 'Changed name.', 15, 1),
(195, '2016-08-08 15:01:56', '4', 'Movie Task Documentation', 2, 'Changed content.', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=24 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(14, 'blog', 'about'),
(20, 'blog', 'conference'),
(21, 'blog', 'contact'),
(16, 'blog', 'education'),
(22, 'blog', 'image'),
(19, 'blog', 'language'),
(17, 'blog', 'music'),
(8, 'blog', 'post'),
(23, 'blog', 'privacy'),
(11, 'blog', 'project'),
(15, 'blog', 'skill'),
(7, 'blog', 'tag'),
(18, 'blog', 'userdata'),
(12, 'blog', 'work'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(13, 'sites', 'site');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-04-16 09:41:59'),
(2, 'auth', '0001_initial', '2015-04-16 09:42:00'),
(3, 'admin', '0001_initial', '2015-04-16 09:42:00'),
(4, 'blog', '0001_initial', '2015-04-16 09:42:01'),
(5, 'sessions', '0001_initial', '2015-04-16 09:42:01'),
(6, 'blog', '0002_auto_20150420_2015', '2015-04-20 14:45:59'),
(7, 'blog', '0003_work', '2015-04-20 15:35:19'),
(8, 'blog', '0002_auto_20150422_2146', '2015-04-22 17:39:34'),
(9, 'blog', '0003_comment', '2015-04-22 17:40:23'),
(10, 'blog', '0004_auto_20150422_2147', '2015-04-22 17:40:39'),
(11, 'sites', '0001_initial', '2015-04-22 17:45:00'),
(12, 'blog', '0005_about', '2015-04-22 19:28:04'),
(13, 'blog', '0006_skill', '2015-04-22 20:46:37'),
(14, 'blog', '0007_education', '2015-04-22 21:34:56'),
(15, 'blog', '0008_auto_20150423_1407', '2015-04-23 08:37:26'),
(16, 'blog', '0009_auto_20150423_1409', '2015-04-23 08:39:34'),
(17, 'blog', '0010_auto_20150423_1437', '2015-04-23 09:07:38'),
(18, 'blog', '0011_auto_20150423_1455', '2015-04-23 09:26:04'),
(19, 'blog', '0012_auto_20150424_2120', '2015-04-24 15:50:22'),
(20, 'blog', '0013_auto_20150516_0131', '2015-05-15 20:01:36'),
(21, 'blog', '0014_auto_20150516_0144', '2015-05-15 20:14:38'),
(22, 'blog', '0002_auto_20150610_1623', '2015-06-10 10:53:26'),
(23, 'blog', '0002_post_image', '2015-06-10 11:30:46'),
(24, 'blog', '0003_image', '2015-06-10 12:12:39'),
(25, 'blog', '0004_auto_20150610_1803', '2015-06-10 12:33:42'),
(26, 'blog', '0005_auto_20150612_1554', '2015-06-12 10:24:47'),
(27, 'blog', '0006_auto_20150612_1638', '2015-06-12 11:08:30'),
(28, 'blog', '0002_auto_20151007_2034', '2015-10-07 15:19:26'),
(29, 'contenttypes', '0002_remove_content_type_name', '2015-10-08 07:49:21'),
(30, 'auth', '0002_alter_permission_name_max_length', '2015-10-08 07:49:21'),
(31, 'auth', '0003_alter_user_email_max_length', '2015-10-08 07:49:21'),
(32, 'auth', '0004_alter_user_username_opts', '2015-10-08 07:49:21'),
(33, 'auth', '0005_alter_user_last_login_null', '2015-10-08 07:49:21'),
(34, 'auth', '0006_require_contenttypes_0002', '2015-10-08 07:49:21'),
(35, 'blog', '0003_privacy', '2016-07-18 14:08:26');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('11vbuq9ikypp2pkfl3eez3ssjqtdso3m', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-08-01 14:05:32'),
('2frpnzgb7ynpprwtjuu9ebttl6km1gyn', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-02-12 15:29:10'),
('4xc0hxgbyx8xxz16wjyo1p8mfna65359', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-04-30 09:46:27'),
('5i7539ho6ej41cbldk2j1ihvug7hfhfg', 'OTMyZmJhMzEzOGU2MTI1MWQwOWIxZGE3ZmZhNDMyZjI2ZjE5YzY4Mjp7fQ==', '2015-05-12 09:26:48'),
('6x24vq5psxgdqe3o7zcmkr5i8yds40lc', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-05-23 08:52:21'),
('7a00bl430i7lvg6bh0laa6arpxptiqmr', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-02-16 11:21:38'),
('abudx2dqmb89sj4swbfae51xtp61aucb', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-07-27 12:55:38'),
('b093dqccyt3ymll1mv6wiwwn66ac5d66', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-06-08 10:07:52'),
('bcp4diajhjq6glfa4r26k1lqfanhyh9c', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-16 07:44:15'),
('c168qltpzzqkner2o9tn0mlwswrkrdme', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-12 14:00:10'),
('c8om1p30520e3syuculctgdd899zlm6l', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-10-21 15:36:44'),
('ckc011v97xd6vvzjdfn4a405gartw4k3', 'OTMyZmJhMzEzOGU2MTI1MWQwOWIxZGE3ZmZhNDMyZjI2ZjE5YzY4Mjp7fQ==', '2015-07-10 12:00:27'),
('gy5hb3zly38bg8bcxkqeeljiaojsn176', 'OTMyZmJhMzEzOGU2MTI1MWQwOWIxZGE3ZmZhNDMyZjI2ZjE5YzY4Mjp7fQ==', '2015-05-12 09:26:17'),
('ifvkngk7311bvbvxvgio56m08c9fbhcs', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-06-24 10:46:51'),
('jqp3jlbu377jrq3npsq2chyszqejo4qj', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-06-05 12:39:01'),
('kis9clt586oi5qbrbalko5n5dc9ltuzb', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-06-13 14:42:14'),
('lxdmjv1zjrn89yttl8fyicds3fdyie3w', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-06-17 10:34:10'),
('otuf8qitph6e07gcoc6itqclif258hbz', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-04-02 10:04:05'),
('p0tia9t0f2zh5opdce5caomsjjddfxib', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-06-17 10:27:31'),
('pp2egefoww234ztaemhwuj0h65ho85ny', 'MGI0NDg5YmQzOWE2YWExOTExNzc1OWVlYTJiOGQ4ODU0N2I0YTg3Yzp7ImVtYWlsIjoibmFrQHJhLmNvbSIsIl9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2lkIjoxLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIm5hbWUiOiJOYWpuIn0=', '2015-04-30 10:08:33'),
('qcb8pktbyk1ije9wn283mw96ctbz6eue', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-03-25 12:15:17'),
('sf7or6z03go305gf7ea1vszzodrmgrfj', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-08-20 12:12:47'),
('udst6m53pv3qytl2dzqhsw5q83lxtfv6', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-02-28 19:25:13'),
('vfe8sn420v90085d0519emn0hn9lk0dm', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-05-29 18:10:52'),
('vnkc6kemrnxhuhnhhj9p8t47m7292ih4', 'ZWJiY2ZmYjZkOWUzZmUzZDQ5NTlmZDMzMTg2M2IzZjI3MjU2ZDVhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4MmMxZmJmODk4MTVkYmNiZGIxNzI5M2ZiYzAzOWVlM2Q4NTMyYmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-02-11 13:19:24'),
('z0alfqw93oked55oajufa1muxvi8yl99', 'OTMyZmJhMzEzOGU2MTI1MWQwOWIxZGE3ZmZhNDMyZjI2ZjE5YzY4Mjp7fQ==', '2015-05-21 20:00:52'),
('z162o7jtsamemtc86oz9znta79e828x0', 'NTQ0N2M0YTViODE2YmRmOTQ0YjBiYzhiY2IwNDkxY2M2NmJlZmRmNjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM2ZjM3NzU2MTBkNTU2MmE4MTRjNTAxOWJjZWQ2MDAzN2Y0NzMyMTIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-06-24 11:34:05');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'rohanroy.com', 'Rohan Roy');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blog_post`
--
ALTER TABLE `blog_post`
  ADD CONSTRAINT `blog_post_author_id_5d99f39cce94a67b_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blog_post_tags`
--
ALTER TABLE `blog_post_tags`
  ADD CONSTRAINT `blog_post_tags_post_id_f385a4e5bab89b5_fk_blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `blog_post` (`id`),
  ADD CONSTRAINT `blog_post_tags_tag_id_12f83b29ba9842bc_fk_blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
