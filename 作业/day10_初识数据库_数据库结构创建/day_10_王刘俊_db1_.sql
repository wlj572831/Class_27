
-- ----------------------------
-- 创建wlj_db库
-- ----------------------------
DROP DATABASE IF EXISTS `wlj_db`;
CREATE DATABASE IF NOT EXISTS wlj_db default charset utf8 COLLATE utf8_general_ci;
USE wlj_db;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- 创建class表 cid为主键
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- 批量插入class表数据
-- ----------------------------
INSERT INTO `class` VALUES (1, '三年二班');
INSERT INTO `class` VALUES (2, '三年三班');
INSERT INTO `class` VALUES (3, '一年二班');

-- ----------------------------
-- 创建course表 cid为主键
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`cid`) USING BTREE,
  INDEX `fk_course_teacher`(`teacher_id`) USING BTREE,
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`tid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- 批量插入course表数据
-- ----------------------------
INSERT INTO `course` VALUES (1, '生物', 1);
INSERT INTO `course` VALUES (2, '物理', 1);
INSERT INTO `course` VALUES (3, '体育', 3);

-- ----------------------------
-- 创建score表 sid为主键
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `fk_score_student`(`student_id`) USING BTREE,
  INDEX `fk_score_course`(`course_id`) USING BTREE,
  CONSTRAINT `fk_score_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_score_student` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- 批量插入score表数据
-- ----------------------------
INSERT INTO `score` VALUES (1, 1, 2, 60);
INSERT INTO `score` VALUES (2, 2, 3, 100);
INSERT INTO `score` VALUES (3, 3, 1, 59);

-- ----------------------------
-- 创建student学生表，sid 为主键
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `gender` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_id` int(11) NOT NULL,
  `sname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `fk_class`(`class_id`) USING BTREE,
  CONSTRAINT `fk_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- 批量插入学生数据
-- ----------------------------
INSERT INTO `student` VALUES (1, '女', 1, '钢蛋');
INSERT INTO `student` VALUES (2, '女', 1, '铁锤');
INSERT INTO `student` VALUES (3, '男', 2, '山炮');

-- ----------------------------
-- 创建teacher教师表， tid 为主键
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`tid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- 批量插入教师数据
-- ----------------------------
INSERT INTO `teacher` VALUES (1, '波多');
INSERT INTO `teacher` VALUES (2, '苍空');
INSERT INTO `teacher` VALUES (3, '饭岛');

SET FOREIGN_KEY_CHECKS = 1;

COMMIT;