from main import buildApp

def findComponentUsingId(component, targetId):
    if hasattr(component, "id") and component.id == targetId:
        return component

    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            for child in children:
                result = findComponentUsingId(child, targetId)
                if result is not None:
                    return result
        elif children is not None:
            result = findComponentUsingId(children, targetId)
            if result is not None:
                return result
    return None

def testHeader():
    app = buildApp()
    header = findComponentUsingId(app.layout, "page-header")
    assert header is not None
    assert header.children == "Soul Foods Pink Morsel Sales"

def testVisualisation():
    app = buildApp()
    graph = findComponentUsingId(app.layout, "sales-chart")
    assert graph is not None

def testRegionPicker():
    app = buildApp()
    radioButtons = findComponentUsingId(app.layout, "region-filter")
    assert radioButtons is not None