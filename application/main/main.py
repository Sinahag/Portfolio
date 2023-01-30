import os
from application import db
from flask import render_template, redirect, request, send_file, send_from_directory, session, url_for, flash, Blueprint, Response, make_response
from application.main.models import Post
from flask_login import current_user, login_required
from application.main.forms import PostForm
import codecs

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/index")
@main.route("/home")
def index():
    return render_template("main/index.html", index=True)

# TODO: build blog page which could be for others to share their projects
@main.route("/blog")
# @login_required
def blog():
    return render_template("main/blog.html")

@main.route("/projects")
def projects():
    projects = Post.objects().all()
    images = list()
    for project in projects:
        base64_data = codecs.encode(project.image.thumbnail.read(), 'base64')
        image = base64_data.decode('utf-8')
        images.append(image)
    return render_template("main/projects.html", projects=projects, images = images, numposts=len(projects))

@main.route("/resume")
def resume():
    return send_from_directory('static','files/Resume.pdf')

@main.route("/profile")
@login_required
def profile():
    return render_template("main/profile.html",user=current_user)

@main.route("/project/<int:id>")
@main.route("/project/<string:name>")
def project_viewer(id=None,name=None):
    if not name:
        project = Post.objects(id=id).first()
    else:
        project = Post.objects(title=name).first()
    if not project:
        return render_template("errors/404.html")

    base64_data = codecs.encode(project.image.read(), 'base64')
    image = base64_data.decode('utf-8')

    return render_template("main/project_viewer.html",project=project,image=image)


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
    video_url = request.form.get('video_url')
    github_url = request.form.get('github_url')
    keyword = request.form.get('keyword')
    username =  current_user.name
    num_posts_after_this = Post.objects().count()

    pid = (num_posts_after_this+1)*(num_posts_after_this+2)/2

    total = 0
    for i in Post.objects():
        total += i.id

    path = os.path.join(os.path.abspath(image.filename))
    if len(str(image.filename))>0:
        image.save(path)
    else: 
        flash("Please upload image","error")
        return redirect(url_for('main.projects'))

    new_post = Post(id=(pid-total), 
                    title = title, 
                    image = path,
                    video_url=video_url,
                    description = description, 
                    keyword = keyword,
                    user = username,
                    github_url = github_url)

    try:
        new_post.validate()
    except:
        return redirect(url_for('main.projects'))
    new_post.save()
    return redirect(url_for('main.projects'))

