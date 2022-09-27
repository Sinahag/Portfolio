import os
from application import db
from flask import render_template, redirect, request, url_for, flash, Blueprint, Response
from application.main.models import Post
from flask_login import current_user, login_required
from application.main.forms import PostForm

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/index")
@main.route("/home")
def index():
    return render_template("main/index.html", index=True)


@main.route("/profile")
@login_required
def profile():
    return render_template("main/profile.html",name=current_user.name)

# TODO: build blog page
@main.route("/projects")
# @login_required
def projects(num=3):
    return render_template("main/blog.html", show_per_page=num, Post=Post)

#TODO: Fix retrieval of images from database
@main.route("/project/<int:id>")
@login_required
def project_viewer(id=1):
    image = Post.objects(id=id).first()
    if not image:
        return render_template("errors/404.html")

    return render_template("main/project_viewer.html",image=image)

@main.route("/post")
@login_required
def post(title="New Project"):
    form=PostForm()
    return render_template("main/newpost.html",title=title,form=form)

@main.route("/post", methods=['POST'])
@login_required
def post_post():
    title = request.form.get('title')
    description = request.form.get('description')
    image = request.files.get('image')
    keyword = request.form.get('keyword')
    user = Post.objects(title=title).first()

    if user:
        flash('Email address already exists', "danger")
        return redirect(url_for("main.projects"))
    path = os.path.join(os.path.abspath(image.filename))

    image.save(path)

    new_post = Post(id=Post.objects.count() + 1, 
                    title = title, 
                    image = path,
                    description = description, 
                    keyword = keyword)
    new_post.save()
    return redirect(url_for('main.projects'))

