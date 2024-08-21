# Assignment 2. Web application for uploading images with descriptions

## **General description of the project**                                                                        


**Project name**: `ImageHub`                                                                        

**Project's point**: Develop a Django based web application to upload, store                                                                         
and view images with descriptions.                                                                        

## **Main Functions**:                                                                        

* **Creating user accounts.**                                                                        
* **Uploading images by users.**                                                                        
* **Adding descriptions to images.**                                                                        
* **Editing and deleting images.**                                                                        
* **View a list of uploaded images with descriptions.**                                                                        
* **API for uploading and retrieving images.**                                                                        

## **Project Stack**:

1. **General**                                                                               
* `Stack`: **Python3**, **Django**, **Django REST Framework**.                                                                               
* `DataBases`: **PostgreSQL** \ **MySQL** (and \ or other non-relational DB).                                                                        

---

## **Technical requirements**                                                                        

The application must be deployed in a **Docker** container.                                                                        
Using **Django ORM** to interact with the database.                                                                        
Configuring **Nginx** to serve static files (images).                                                                        


## **Description of database models**                                                                        

1) Model `Image`:                                                                        
* `id`: **Integer** (Primary Key)                                                                        
* `file`: **ImageField** (image file storage)                                                                        
* `description`: **TextField** (image description)                                                                        
* `category`: **ForeignKey** (relationship with the category model)                                                                        
* `user`: **ForeignKey** (relationship with the user model)                                                                        
* `delete`: **BooleanField** (image deletion flag)                                                                        
* `uploaded_at`: **DateTimeField** (date and time of upload)                                                                        
* `updated_at`: **DateTimeField** (date and time of update)                                                                        
* `deleted_at`: **DateTimeField** (date and time of deletion)                                                                        

Model `Category`:                                                                        
* `id`: **Integer** (Primary Key)                                                                        
* `name`: **CharField** (category name)                                                                        
* `created_at`: **DateTimeField** (date and time of creation)                                                                        

---

## **Documentation**                                                                               

1) **README**:                                                                               
Project Description.                                                                               
List of technologies used to write the project.                                                                               
Instructions on how to install and run the application: commands one                                                                                                                                    
by one. How to run the project.                                                                                                                                     
2) **API documentation**:                                                                               
Description of endpoints, request and response formats. Examples of                                                                                                                                                                                                                           
data that must be passed to process requests.                                                                                      

## **Functional requirements**                                                                                                                                                

1) **For the user**:                                                                        
   * **Account registration**                                                                        
       * **As a user, I want to be able to** create an account to utilize the                                                                         
       functionality of the app.                                                                        

   * **Login**                                                                        
       * **As a user, I want to be able to** log in to access my personalized account.                                                                        
   * **Uploading Images**                                                                        
       * **As a user, I want to be able to** upload pictures to share with other users.                                                                        
   * **Viewing Images**                                                                        
       * **As a user, I want to be able to** browse images to see photos uploaded                                                                        
       by other users.                                                                        
   * **Adding descriptions to images**                                                                        
       * **As a user, I want to be able to** add descriptions to my images so that                                                                         
       other users understand the context or history of the image.                                                                        
   * **Editing and deleting my images**                                                                        
       * **As a user, I want to be able to** edit and delete my images to manage my content.                                                                        
2) **For admin**:
   * **User Management**                                                                        
       * **As an administrator, I want to be able to** view, edit, and delete user                                                                         
       accounts to ensure order on the platform.                                                                        
   * **Image Management**                                                                        
       * **As an admin, I want to be able to** view, edit, and delete any images to                                                                        
       keep my content compliant with platform standards.                                                                        


## **CRUD operations**                                                                      
1) **CRUD for user**:                                                                      
`Create`: **Register a new user.**                                                                      
`Read`: **View your profile information**.                                                                      
`Update`: **Update your profile information (e.g., email, password).**                                                                      
`Delete`: **Delete your account.**                                                                      
2) **CRUD for Categories**:                                                                      
`Create`: **Create a new category (administrator only).**                                                                      
`Read`: **View a list of categories.**                                                                      
`Update`: **Edit category name (admin only).**                                                                      
`Delete`: **Delete a category (administrator only).**                                                                      
3) **CRUD for images**:                                                                      
`Create`: **Uploading a new image with a description.**                                                                      
`Read`: **View a list of all uploaded images with descriptions.**                                                                      
`Update`: **Edit the description of an already uploaded image.**                                                                      
`Delete`: **Delete an image.**                                                                      

---

## **Permissions and roles**                                                                      

**Ordinary user**: Upload images, view all images, edit and delete your images.                                                                      
**Administrator**: Manage all images and descriptions.                                                                      

---

## **Security**                                                                               

1) **Authentication**:                                                                               
* Consider implementing an authentication system (e.g. **Token Authentication**).                                                                               

2) **Data Validation**:                                                                               
* Check for correct input data for all operations.                                                                               

---

## **Testing**                                                                               
1) **Unit tests**:                                                                               
* Writing tests to verify the functionality of all **CRUD** operations.                                                                               
2) **Integration tests**:                                                                               
* Testing the interaction of system components.                                                                               


---
### **Rules for working with **Git** for thesis writing and development. Branch organization**                                                                               
`One task - one branch`: You should create a separate branch from the                                                                                
main for each new task or functionality.                                                                                
The name of the branch should reflect the nature of the task.                                                                               

`Prohibit direct changes to the main`: All changes should be pushed into                                                                                
the main via **Pull Requests (PR)** after review and approval by other team members.                                                                               


**Commits**                                                                               
* `Many commits`: Make commits frequently to track progress and facilitate                                                                               
possible debugging.                                                                               
* `Informative commits`: Each commit should contain a clear and concise                                                                               
description of the changes made.                                                                               
* `Prefix commit system`:
    * `doc`: To add or modify documentation.                                                                               
    * `feat`: To add new functionality.                                                                               
    * `fix`: For bug fixes or debugging.                                                                               

**Working with Pull Requests (PR)**                                                                                                                                                              
* `PR Description`: Each PR should contain a detailed description of the                                                                                
changes made and references to relevant tasks or requirements.                                                                               
* `Code-review`: Prior to merging with the main, the PR should be                                                                               
code-reviewed by at least one other team member.                                                                               
* `Testing`: Before creating a PR, make sure your code passes all                                                                                
tests and meets coding standards.                                                                               

**Regular updates**
`Synchronize with main`: Regularly update your working branches by                                                                                
synchronizing them with the main branch of main to avoid merge conflicts.                                                                               

---

### **Additionally**                                                                               
**Docker и Nginx**:                                                                               
* Project containerization using [**Docker**](https://www.docker.com/).                                                                               
* [**Nginx**](https://www.nginx.com/) to serve static files.                                                               
