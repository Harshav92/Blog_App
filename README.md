# Blog_App
# Shopping-clone Back-end web services implementation

## Services implemented
* [Register](#register)
* [Login](#login)
* [create blog](#create-blog)
* [show blogs](#show-blogs)
* [update-blogs](#update-blogs)


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