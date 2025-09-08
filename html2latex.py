def html_to_latex():
    html_str = input('Please enter a HTML string: ')
    latex_str = html_str
    latex_str = latex_str.replace('&ldquo;','``')
    latex_str = latex_str.replace('&rdquo;','"')
    latex_str = latex_str.replace('&amp;','&')
    latex_str = latex_str.replace('&gt;','>')
    latex_str = latex_str.replace('&lt;','<')
    latex_str = latex_str.replace('&quot;','"')
    latex_str = latex_str.replace('&apos;',"'")
    latex_str = latex_str.replace('{','\{')
    latex_str = latex_str.replace('}','\}')
    latex_str = latex_str.replace('%','\%')
    print(latex_str)

html_to_latex()
