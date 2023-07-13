from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return None

    # template = get_template(template_src)
    # html = template.render(context_dict)
    # response = HttpResponse(content_type='application/pdf')
    # pdf_status = pisa.CreatePDF(html, dest=response)

    # if pdf_status.err:
    #     return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

    # return response