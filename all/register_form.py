login_form="""
<form action="/register" method="post">
        <div class="form-group">
            <input autofocus class="form-control" name="username" placeholder="Username" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="password" placeholder="Password" type="password"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="confirm" placeholder="Confirm" type="password"/>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-default">Sign up</button>
        </div>
</form>
<div>
    or <a href="/login">login</a>
</div>
"""
