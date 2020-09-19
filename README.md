# Blog_App
# Shopping-clone Back-end web services implementation

## Services implemented
* [Register](#register)
* [Login](#login)
* [create blog](#create-blog)
* [show blogs](#show-blogs)
* [update blogs](#update-blogs)
* [add comment](#add-comment)
* [show commnet](#show-comment)
* [sub comment](#sub-comment)
* [delete](#delete-comment)


### Register service
* This service takes five inputs "name" , "email" ,"password" 
* url_path : /user/register

### Login Service
* takes two inputs "email"/"phone_no" and "password"
* url_path : /user/login

### create blog
* url_path : /blog/create
* takes author_id, description, content, name as inputs

### show blogs
* url_path : /blog/list
* show all the blogs

### update blogs
* url_path : /blog/update. only original author can update
* takes blog_id , user_id , content

### add comment
* url_path : /comment/add
* takes comment , user_id , blog_id as inputs
* Method : "POST"


### show comment
* url_path : /comment/show
* Takes blog_id as input
* Method : "GET"

### sub-comment
* url_path : /comment/subcomment
* takes comment_id , user_id , comment as input
* Method : "POST"

### Delete
* url_path : /comment/delete
* takes comment_id and user_id as request
* Method : "DELETE"
