# Mentor Advice — sharvilak_writes Blog

This is your learning journal for this project. Come back here when you forget why something works or where to go next.

---

## What This Project Is

A personal blog built with Django. You write posts, people read them.
Stack: Python + Django + SQLite (for now) + HTML templates.

---

## The Django Mental Model (tattoo this)

```
Browser Request
    → urls.py         (which view handles this URL?)
    → views.py        (what data do I need? what template do I use?)
    → models.py       (talk to the database)
    → template (HTML) (render and send back)
```

Every Django app you ever build follows this flow. Learn to read it backwards too — start from the template and trace up to the URL.

---

## What Each File Does

| File | Job |
|------|-----|
| `models.py` | Defines DB tables as Python classes. One class = one table. |
| `views.py` | Business logic. Gets data, picks template, returns response. |
| `urls.py` | Maps URLs to views. Like a traffic router. |
| `admin.py` | Register models here → manage data at `/admin/`. |
| `settings.py` | App-wide config. Installed apps, DB, secret key, etc. |
| `templates/` | HTML files. Django fills in `{{ variables }}` before sending. |

---

## Concepts You've Already Used

### Class-Based Views (CBVs)
Django gives you pre-built view classes. You extend them instead of writing everything from scratch.

```python
class PostListView(ListView):   # ListView = "show a list of objects"
    model = Post                # which model?
    template_name = '...'      # which HTML?
    context_object_name = 'posts'  # name in the template for the list
```

Django's built-in CBVs you're using:
- `ListView` — list of objects
- `DetailView` — single object
- `CreateView` — form to create object
- `UpdateView` — form to edit object
- `DeleteView` — confirm and delete object

**Why CBVs?** Less code. Django handles GET/POST logic for you.

### ForeignKey (Relationships)
```python
author = models.ForeignKey(User, on_delete=models.CASCADE)
```
- Post belongs to a User. Many posts → one user.
- `on_delete=CASCADE` → delete user → delete their posts too.
- SQL equivalent: `FOREIGN KEY (author_id) REFERENCES auth_user(id)`

### `get_absolute_url()`
Model knows its own URL. Django's CreateView/UpdateView auto-redirect there after save. Convention — always define this on models that have detail pages.

### `Meta: ordering`
```python
class Meta:
    ordering = ['-date_posted']  # minus = descending (newest first)
```
DB always returns in this order. No `.order_by()` needed in views.

### `LoginRequiredMixin` (commented out for now)
Mixin = a class you inherit to add behaviour. `LoginRequiredMixin` redirects unauthenticated users to login page. Add it back when you're ready for auth.

---

## Things Commented Out (and Why)

Auth (login/logout) is scaffolded but disabled. You're learning the core CRUD loop first. Good call — auth adds complexity, tackle it after the blog actually works.

When you're ready to re-enable:
1. Uncomment `urls.py` login/logout paths
2. Uncomment `settings.py` `LOGIN_REDIRECT_URL` and `LOGIN_URL`
3. In `views.py` — re-add `LoginRequiredMixin` to Create/Update/Delete views
4. In `PostCreateView.form_valid` — swap `User.objects.first()` back to `self.request.user`
5. Re-add `UserPassesTestMixin` + `test_func` to Update/Delete (so only authors can edit their posts)

---

## What To Build Next (Suggested Order)

1. **Get it running** — `python manage.py migrate` → `python manage.py createsuperuser` → `python manage.py runserver` → go to `/` and `/admin/`
2. **Add sample posts via admin** — see them show up on the list page
3. **Style the templates** — make it look like your blog, not a Django skeleton
4. **Categories or tags** — another model, another ForeignKey
5. **Search** — filter posts by keyword
6. **Auth** — login/logout/register (uncomment the TODO items above)
7. **Deploy** — Railway, Render, or PythonAnywhere (free tiers exist)

---

## Commands You'll Use Constantly

```bash
python manage.py runserver          # start dev server at localhost:8000
python manage.py makemigrations     # after changing models.py, generate migration file
python manage.py migrate            # apply migrations to DB
python manage.py createsuperuser    # create admin user
python manage.py shell              # Python shell with Django loaded (for debugging)
```

---

## When You Come Back After a Break

1. Read this file.
2. Run `git log --oneline` — see where you left off.
3. Run `python manage.py runserver` — see if it still works.
4. Check `TODO` comments in code — they're breadcrumbs you left yourself.

---

## The Bigger Picture

This blog teaches you the same patterns used in real Django apps — just smaller scale. Every concept here (models, views, URLs, templates, auth, migrations) appears in production codebases. The knowledge transfers directly.

Finish this. Then look at a real project and you'll recognise everything.
