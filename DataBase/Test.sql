select avg(degree) from score where cno like '3%' and group by cno having count(*) >5;
select sname,cno,degree from students inner join score where students.sno=score.sno;
select sno,cname,degreee from score inner join couses where socre.cno = course.cno;
select sname,cname,degree from socre inner join course on score.cno = course.cno