date: 2022-09-25 10:17:17
author: Jerry Su
slug: python-docx-using-lxml
title: Python docx using lxml
category: 
tags: Python, Docx, lxml
summary: Reason is the light and the light of life.
toc: show


```python
import docx
import lxml
import zipfile
```


```python
# load docx file
docx_obj = docx.Document("/var/www/blog/content/cache/template.docx")
paras = docx_obj.paragraphs
```


```python
# traverse all runs of the specified paragraph idx 6.
para = paras[6]
for idx, run in enumerate(para.runs):
    print(f"run {idx}: {run.text}")
```

    run 0: 专利的
    run 1: 技术方案写的尽可能详细
    run 2: ，以，对于不涉及具体的代码或者公式，只需写明
    run 3: 技术实现流程
    run 4: 即可，具体如下：



```python
# traverse all child nodes of the specified paragraph idx 6.
para = paras[6]._p
for idx, child in enumerate(para):
    print(f"child{idx}: {child}, text: {child.text}, tag: {child.tag}")
```

    child0: <CT_PPr '<w:pPr>' at 0x7f7e46ee9720>, text: None, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr
    child1: <CT_R '<w:r>' at 0x7f7e46ef7e50>, text: 专利的, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}r
    child2: <CT_R '<w:r>' at 0x7f7e46e87ae0>, text: 技术方案写的尽可能详细, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}r
    child3: <CT_R '<w:r>' at 0x7f7e46e8b090>, text: ，以，对于不涉及具体的代码或者公式，只需写明, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}r
    child4: <CT_R '<w:r>' at 0x7f7e46e8b0e0>, text: 技术实现流程, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}r
    child5: <CT_R '<w:r>' at 0x7f7e46ee9090>, text: 即可，具体如下：, tag: {http://schemas.openxmlformats.org/wordprocessingml/2006/main}r



```python

```

Parent and Child: childs of the parent is list.

https://lxml.de/apidoc/lxml.etree.html#lxml.etree.ElementBase


```python
# get child as a list
child1 = para[1]
child1
```




    <CT_R '<w:r>' at 0x7f7e46ef7e50>




```python
# get next child
child2 = child1.getnext()
child2
```




    <CT_R '<w:r>' at 0x7f7e46e87860>




```python
# get previoue child
child0 = child1.getprevious()
child0
```




    <CT_PPr '<w:pPr>' at 0x7f7e46ee9720>




```python
# get child1's parent
parent_of_child1 = child1.getparent()
parent_of_child1
```




    <CT_P '<w:p>' at 0x7f7e46edd680>




```python
# get child2's parent
parent_of_child2 = child2.getparent()
parent_of_child2
```




    <CT_P '<w:p>' at 0x7f7e46edd680>




```python
parent_of_child1 is parent_of_child2
```




    True




```python
parent_of_child1 is para
```




    True




```python

```


```python
para.getparent()
```




    <CT_Body '<w:body>' at 0x7f7e46eff4f0>




```python
para.attrib
```




    {'{http://schemas.microsoft.com/office/word/2010/wordml}paraId': '14F4DE98', '{http://schemas.microsoft.com/office/word/2010/wordml}textId': '299587E1', '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rsidR': '00BE3E87', '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rsidRDefault': '00000000'}




```python

```


```python
paras
```




    [<docx.text.paragraph.Paragraph at 0x7f7e46eda3d0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edaf10>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda5b0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda7f0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda310>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edafd0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edaee0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edaf40>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda8b0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edad00>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edae80>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda490>,
     <docx.text.paragraph.Paragraph at 0x7f7e46eda430>,
     <docx.text.paragraph.Paragraph at 0x7f7e46edad30>,
     <docx.text.paragraph.Paragraph at 0x7f7e46ed9490>,
     <docx.text.paragraph.Paragraph at 0x7f7e46ed90a0>,
     <docx.text.paragraph.Paragraph at 0x7f7e46ed9040>]




```python
para0 = paras[0]
para0
```




    <docx.text.paragraph.Paragraph at 0x7f7e46eda3d0>




```python
runs_of_para0 = para0.runs
runs_of_para0
```




    [<docx.text.run.Run at 0x7f7e46b6db80>,
     <docx.text.run.Run at 0x7f7e46b6d9a0>,
     <docx.text.run.Run at 0x7f7e46b6df40>,
     <docx.text.run.Run at 0x7f7e46b6dc40>]




```python
run1_of_para0 = runs_of_para0[1]
run1_of_para0
```




    <docx.text.run.Run at 0x7f7e46b6d9a0>




```python

```


```python

```


```python
para0_xml = para0._p.xml
print(para0_xml)
```

    <w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" w14:paraId="64691129" w14:textId="0EB0539D" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
      <w:pPr>
        <w:jc w:val="center"/>
        <w:rPr>
          <w:b/>
          <w:sz w:val="32"/>
          <w:szCs w:val="32"/>
        </w:rPr>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:hint="eastAsia"/>
          <w:b/>
          <w:sz w:val="32"/>
          <w:szCs w:val="32"/>
        </w:rPr>
        <w:t xml:space="preserve">           </w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:hint="eastAsia"/>
          <w:b/>
          <w:sz w:val="32"/>
          <w:szCs w:val="32"/>
        </w:rPr>
        <w:t>方案模板</w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:hint="eastAsia"/>
          <w:b/>
          <w:sz w:val="32"/>
          <w:szCs w:val="32"/>
        </w:rPr>
        <w:t xml:space="preserve">      </w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="黑体" w:eastAsia="黑体" w:hint="eastAsia"/>
          <w:sz w:val="18"/>
          <w:szCs w:val="18"/>
        </w:rPr>
        <w:t>编号_____________</w:t>
      </w:r>
    </w:p>
    



```python
for idx, run in enumerate(para0.runs):
    print(f"run {idx}: {run.text}")
    print(run._r.xml)
```

    run 0:            
    <w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
      <w:rPr>
        <w:rFonts w:hint="eastAsia"/>
        <w:b/>
        <w:sz w:val="32"/>
        <w:szCs w:val="32"/>
      </w:rPr>
      <w:t xml:space="preserve">           </w:t>
    </w:r>
    
    run 1: 方案模板
    <w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
      <w:rPr>
        <w:rFonts w:hint="eastAsia"/>
        <w:b/>
        <w:sz w:val="32"/>
        <w:szCs w:val="32"/>
      </w:rPr>
      <w:t>方案模板</w:t>
    </w:r>
    
    run 2:       
    <w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
      <w:rPr>
        <w:rFonts w:hint="eastAsia"/>
        <w:b/>
        <w:sz w:val="32"/>
        <w:szCs w:val="32"/>
      </w:rPr>
      <w:t xml:space="preserve">      </w:t>
    </w:r>
    
    run 3: 编号_____________
    <w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">
      <w:rPr>
        <w:rFonts w:ascii="黑体" w:eastAsia="黑体" w:hint="eastAsia"/>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
      </w:rPr>
      <w:t>编号_____________</w:t>
    </w:r>
    



```python

```

XML -> lxml

lxml: lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.

[https://lxml.de](https://lxml.de)

[https://github.com/lxml/lxml](https://github.com/lxml/lxml)


```python
document = zipfile.ZipFile("/var/www/blog/content/cache/template.docx")
docx_xml = document.read("word/document.xml")
e_tree = lxml.etree.fromstring(docx_xml)
print(lxml.etree.tostring(e_tree, encoding='unicode', pretty_print=True))
```

    <w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 w16se w16cid w16 w16cex w16sdtdh wp14">
      <w:body>
        <w:tbl>
          <w:tblPr>
            <w:tblpPr w:leftFromText="180" w:rightFromText="180" w:vertAnchor="page" w:horzAnchor="margin" w:tblpXSpec="center" w:tblpY="2281"/>
            <w:tblW w:w="9322" w:type="dxa"/>
            <w:tblBorders>
              <w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>
              <w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>
              <w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>
              <w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>
              <w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>
              <w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>
            </w:tblBorders>
            <w:tblLayout w:type="fixed"/>
            <w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>
          </w:tblPr>
          <w:tblGrid>
            <w:gridCol w:w="2405"/>
            <w:gridCol w:w="2520"/>
            <w:gridCol w:w="2271"/>
            <w:gridCol w:w="2126"/>
          </w:tblGrid>
          <w:tr w:rsidR="00BE3E87" w14:paraId="56E02CD6" w14:textId="77777777">
            <w:trPr>
              <w:trHeight w:val="455"/>
            </w:trPr>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2405" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="2A8D3193" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>发明名称</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="6917" w:type="dxa"/>
                <w:gridSpan w:val="3"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="05B39ECF" w14:textId="0829E535" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                    <w:lang w:eastAsia="zh-Hans"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:szCs w:val="21"/>
                    <w:lang w:eastAsia="zh-Hans"/>
                  </w:rPr>
                  <w:t>装置</w:t>
                </w:r>
              </w:p>
            </w:tc>
          </w:tr>
          <w:tr w:rsidR="00BE3E87" w14:paraId="74733373" w14:textId="77777777">
            <w:trPr>
              <w:trHeight w:val="455"/>
            </w:trPr>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2405" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="7124EC13" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>所属项目</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="6917" w:type="dxa"/>
                <w:gridSpan w:val="3"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="3081890B" w14:textId="2F70FCE0" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>业务项目</w:t>
                </w:r>
              </w:p>
            </w:tc>
          </w:tr>
          <w:tr w:rsidR="00BE3E87" w14:paraId="5F752D79" w14:textId="77777777">
            <w:trPr>
              <w:trHeight w:val="456"/>
            </w:trPr>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2405" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="0289B56C" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>所在部门</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2520" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="7801A069" w14:textId="08ECB4D1" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="left"/>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                    <w:lang w:eastAsia="zh-Hans"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:szCs w:val="21"/>
                    <w:lang w:eastAsia="zh-Hans"/>
                  </w:rPr>
                  <w:t>事业部</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2271" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="7173D47B" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>直属上级或所在团队</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2126" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="03AB58AA" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00BE3E87">
                <w:pPr>
                  <w:jc w:val="left"/>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
              </w:p>
            </w:tc>
          </w:tr>
          <w:tr w:rsidR="00BE3E87" w14:paraId="6AE03D42" w14:textId="77777777">
            <w:trPr>
              <w:trHeight w:val="461"/>
            </w:trPr>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2405" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="2D5E723F" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>技术联系人（撰写人）</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2520" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="1B5194F5" w14:textId="027FD55D" w:rsidR="00BE3E87" w:rsidRDefault="00735EE8">
                <w:pPr>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>j</w:t>
                </w:r>
                <w:r>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>erry</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2271" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="23CC4C14" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>技术联系人联系电话</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2126" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="6F8F6345" w14:textId="2FDDCF66" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>170</w:t>
                </w:r>
              </w:p>
            </w:tc>
          </w:tr>
          <w:tr w:rsidR="00BE3E87" w14:paraId="11041367" w14:textId="77777777">
            <w:trPr>
              <w:trHeight w:val="453"/>
            </w:trPr>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2405" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="379AFC19" w14:textId="1653D816" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>技术号</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2520" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="4FC60CF2" w14:textId="66D8E19B" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>15cf</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2271" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="7BEB6CCA" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                    <w:b/>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>技术联系人电子邮件</w:t>
                </w:r>
              </w:p>
            </w:tc>
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="2126" w:type="dxa"/>
                <w:vAlign w:val="center"/>
              </w:tcPr>
              <w:p w14:paraId="11B96929" w14:textId="6B6A44A8" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
                <w:pPr>
                  <w:jc w:val="center"/>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                </w:pPr>
                <w:proofErr w:type="spellStart"/>
                <w:r>
                  <w:rPr>
                    <w:szCs w:val="21"/>
                  </w:rPr>
                  <w:t>cheny</w:t>
                </w:r>
                <w:proofErr w:type="spellEnd"/>
              </w:p>
            </w:tc>
          </w:tr>
        </w:tbl>
        <w:p w14:paraId="64691129" w14:textId="0EB0539D" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:jc w:val="center"/>
            <w:rPr>
              <w:b/>
              <w:sz w:val="32"/>
              <w:szCs w:val="32"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="32"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t xml:space="preserve">           </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="32"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t>方案模板</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="32"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t xml:space="preserve">      </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="黑体" w:eastAsia="黑体" w:hint="eastAsia"/>
              <w:sz w:val="18"/>
              <w:szCs w:val="18"/>
            </w:rPr>
            <w:t>编号_____________</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="2DC43B52" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体"/>
              <w:b/>
              <w:sz w:val="28"/>
              <w:szCs w:val="32"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="28"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t>技术交底书填写注意事项：</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="5C248211" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t xml:space="preserve"> 1.</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:tab/>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t>整体要求</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="7F9EB8BD" w14:textId="0E7092F1" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>是技术方案的实现说明，主要写明发明目的，实现方案，带来的技术效果，进一步可以通过流程图等方式说明技术的架构和实现方法步骤，不能仅有原理或功能介绍。</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="07222074" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00BE3E87">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
        </w:p>
        <w:p w14:paraId="4343A3EF" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:ind w:firstLineChars="50" w:firstLine="120"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t>2.</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:tab/>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t>具体要求</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="14F4DE98" w14:textId="299587E1" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>专利的</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:color w:val="FF0000"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>技术方案写的尽可能详细</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>，以，对于不涉及具体的代码或者公式，只需写明</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:color w:val="FF0000"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>技术实现流程</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>即可，具体如下：</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="110C2DBC" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>（</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>1</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>）已上线的技术需将技术实现细节进行介绍，对技术诀窍可以采取一定的手段隐藏；</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="2D89725C" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00BE3E87">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
        </w:p>
        <w:p w14:paraId="0CF50060" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t xml:space="preserve">3.  </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t>对现有技术的初步检索要求：</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="2E1C2B42" w14:textId="26278826" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>由于专利授权的前提是申请时不存内外现有技术（包括：已发表的论文、期刊，已经公开的专利、已经公开使用的介绍等），以及业界类似产品，分析跟现有技术的区别。</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="09B4484A" w14:textId="559EED59" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="400" w:lineRule="exact"/>
            <w:ind w:firstLineChars="200" w:firstLine="420"/>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t>如果该发明评估通过，后续会由外部律师进行的，则终止申请。</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="53824453" w14:textId="19AA7757" w:rsidR="00BE3E87" w:rsidRPr="00062AFD" w:rsidRDefault="00000000" w:rsidP="00062AFD">
          <w:pPr>
            <w:jc w:val="left"/>
            <w:rPr>
              <w:b/>
              <w:szCs w:val="21"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:hint="eastAsia"/>
              <w:b/>
              <w:szCs w:val="21"/>
            </w:rPr>
            <w:t xml:space="preserve">   </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:hint="eastAsia"/>
              <w:b/>
              <w:color w:val="000000" w:themeColor="text1"/>
              <w:sz w:val="28"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t>2.1 本发明提供的完整技术实现方案</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="478413F2" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="360" w:lineRule="auto"/>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体"/>
              <w:b/>
              <w:color w:val="000000" w:themeColor="text1"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体"/>
              <w:b/>
              <w:color w:val="000000" w:themeColor="text1"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
            </w:rPr>
            <w:t xml:space="preserve">2.1.1 </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:hint="eastAsia"/>
              <w:b/>
              <w:color w:val="000000" w:themeColor="text1"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
            <w:t>本发明的功能模块概述</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="30FE050E" w14:textId="77777777" w:rsidR="00BE3E87" w:rsidRDefault="00000000">
          <w:pPr>
            <w:spacing w:line="360" w:lineRule="auto"/>
            <w:ind w:firstLineChars="200" w:firstLine="480"/>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia" w:hint="eastAsia"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
            <w:t>本发明主要实现四个功能模块：</w:t>
          </w:r>
        </w:p>
        <w:p w14:paraId="1C14B145" w14:textId="1E9DA85D" w:rsidR="00BE3E87" w:rsidRDefault="00062AFD">
          <w:pPr>
            <w:spacing w:line="360" w:lineRule="auto"/>
            <w:ind w:firstLineChars="200" w:firstLine="480"/>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia"/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia"/>
              <w:noProof/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
            <w:drawing>
              <wp:inline distT="0" distB="0" distL="0" distR="0" wp14:anchorId="2150C723" wp14:editId="60EA5ACE">
                <wp:extent cx="3327400" cy="1968500"/>
                <wp:effectExtent l="0" t="0" r="0" b="0"/>
                <wp:docPr id="1" name="图片 1"/>
                <wp:cNvGraphicFramePr>
                  <a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>
                </wp:cNvGraphicFramePr>
                <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
                  <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                    <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
                      <pic:nvPicPr>
                        <pic:cNvPr id="1" name="图片 1"/>
                        <pic:cNvPicPr/>
                      </pic:nvPicPr>
                      <pic:blipFill>
                        <a:blip r:embed="rId7"/>
                        <a:stretch>
                          <a:fillRect/>
                        </a:stretch>
                      </pic:blipFill>
                      <pic:spPr>
                        <a:xfrm>
                          <a:off x="0" y="0"/>
                          <a:ext cx="3327400" cy="1968500"/>
                        </a:xfrm>
                        <a:prstGeom prst="rect">
                          <a:avLst/>
                        </a:prstGeom>
                      </pic:spPr>
                    </pic:pic>
                  </a:graphicData>
                </a:graphic>
              </wp:inline>
            </w:drawing>
          </w:r>
        </w:p>
        <w:p w14:paraId="6285D335" w14:textId="11F2EF3B" w:rsidR="00BE3E87" w:rsidRPr="00062AFD" w:rsidRDefault="00000000" w:rsidP="00062AFD">
          <w:pPr>
            <w:spacing w:line="360" w:lineRule="auto"/>
            <w:ind w:firstLine="420"/>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia"/>
              <w:b/>
              <w:bCs/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:asciiTheme="majorEastAsia" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorEastAsia" w:cstheme="majorEastAsia" w:hint="eastAsia"/>
              <w:b/>
              <w:bCs/>
              <w:sz w:val="24"/>
              <w:szCs w:val="24"/>
              <w:lang w:eastAsia="zh-Hans"/>
            </w:rPr>
            <w:t>一、数据预处理模块：</w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="仿宋_GB2312" w:eastAsia="仿宋_GB2312" w:hAnsi="新宋体" w:hint="eastAsia"/>
              <w:sz w:val="28"/>
              <w:szCs w:val="32"/>
              <w:u w:val="single"/>
            </w:rPr>
            <w:t xml:space="preserve">                                             </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="仿宋_GB2312" w:eastAsia="仿宋_GB2312" w:hAnsi="新宋体" w:hint="eastAsia"/>
              <w:b/>
              <w:sz w:val="28"/>
              <w:szCs w:val="32"/>
            </w:rPr>
            <w:t xml:space="preserve">                                                                          </w:t>
          </w:r>
        </w:p>
        <w:sectPr w:rsidR="00BE3E87" w:rsidRPr="00062AFD">
          <w:headerReference w:type="default" r:id="rId8"/>
          <w:footerReference w:type="even" r:id="rId9"/>
          <w:footerReference w:type="default" r:id="rId10"/>
          <w:pgSz w:w="11906" w:h="16838"/>
          <w:pgMar w:top="1440" w:right="1230" w:bottom="1440" w:left="1230" w:header="851" w:footer="992" w:gutter="0"/>
          <w:cols w:space="425"/>
          <w:docGrid w:type="lines" w:linePitch="312"/>
        </w:sectPr>
      </w:body>
    </w:document>
    

