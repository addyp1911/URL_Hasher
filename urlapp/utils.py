from django.core.paginator import EmptyPage


def url_validator(value):
    """A custom method to validate any website url """

    import re
    regex = re.compile(
            r'^https?://|www\.|https?://www\.|http?://www\.' # http://www. or https:// or www.
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|' #domain...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if value and not regex.match(value):
        raise AssertionError("The website url is invalid")
    return value

def paginate(data, paginator, pagenumber):
    """
    This method to create the paginated results in Search view.
    """

    if int(pagenumber) > paginator.num_pages:
        raise ValidationError("Not enough pages", code=404)
    try:
        previous_page_number = paginator.page(pagenumber).previous_page_number()
    except EmptyPage:
        previous_page_number = None
    try:
        next_page_number = paginator.page(pagenumber).next_page_number()
    except EmptyPage:
        next_page_number = None
    return data

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def hit_count(request):
    if not request.session.session_key:
        request.session.save()
    s_key = request.session.session_key
    ip = get_client_ip(request)
    url, url_created = UrlHit.objects.get_or_create(url=request.path)

    if url_created:
        track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
        if created:
            url.increase()
            request.session[ip] = ip
            request.session[request.path] = request.path
    else:
        if ip and request.path not in request.session:
            track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
            if created:
                url.increase()
                request.session[ip] = ip
                request.session[request.path] = request.path
    return url.hits