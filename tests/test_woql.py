import pytest
from woqlclient import WOQLQuery

class TestWoqlQueries:

    def test_start_properties_values(self):
        woqlObject = WOQLQuery()
        assert woqlObject.chain_ended == False
        assert woqlObject.contains_update == False
        assert woqlObject.vocab['type'] == 'rdf:type'

    def test_limit_method(self):
        woqlObject = WOQLQuery().limit(10)
        assert woqlObject.json()['limit'][0] == 10
        assert woqlObject.json() == { 'limit': [ 10, {} ] }

    def test_start_method(self):
        woqlObject = WOQLQuery().limit(10).start(0)
        jsonObj = {"limit": [10,{"start": [0,{}]}]}
        assert woqlObject.json() == jsonObj

    def test_WOQLnot_method(self):
        woqlObject = WOQLQuery().WOQLnot(WOQLQuery().triple("a", "b", "c"))
        woqlObjectChain = WOQLQuery().WOQLnot().triple("a", "b", "c")
        jsonObj={ 'not': [ { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] } ] }

        print(woqlObject.json())

        assert woqlObject.json() == jsonObj
        assert woqlObjectChain.json() == jsonObj

    def test_WOQLand_method(self):
        woqlObject=WOQLQuery().WOQLand(WOQLQuery().triple("a", "b", "c"),
                                    WOQLQuery().triple("1", "2", "3"))
        jsonObj={ 'and': [ { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] }, { 'triple': [ "doc:1", "scm:2", { "@language": "en", "@value": "3" } ] } ] }

        assert woqlObject.json() == jsonObj

    def test_WOQLor_method(self):
        woqlObject=WOQLQuery().WOQLor(WOQLQuery().triple("a", "b", "c"),
                                    WOQLQuery().triple("1", "2", "3"))
        jsonObj={ 'or': [ { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] }, { 'triple': [ "doc:1", "scm:2", { "@language": "en", "@value": "3" } ] } ] }

        assert woqlObject.json() == jsonObj

    def test_when_method(self):

        woqlObject=WOQLQuery().when(True, WOQLQuery().addClass("id"))
        woqlObjectChain=WOQLQuery().when(True).addClass("id")
        jsonObj={'when': [
                        {"true":[]},
                        {'add_quad': [ 'scm:id', 'rdf:type', 'owl:Class', 'db:schema' ]}
                      ] }

        assert woqlObject.json() == jsonObj
        assert woqlObjectChain.json() == jsonObj

    def test_opt_method(self):

        woqlObject=WOQLQuery().opt(WOQLQuery().triple("a", "b", "c"))
        woqlObjectChain=WOQLQuery().opt().triple("a", "b", "c")

        jsonObj={ 'opt': [ { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] } ] }

        assert woqlObject.json() == jsonObj
        assert woqlObjectChain.json() == jsonObj

    def test_WOQLfrom_method(self):
        WOQLOriginal=WOQLQuery().limit(10)
        woqlObject=WOQLQuery().WOQLfrom("http://dburl", WOQLOriginal)
        woqlObjectChain=WOQLQuery().WOQLfrom("http://dburl").limit(10)

        jsonObj={ 'from': [ 'http://dburl', { 'limit': [ 10, {} ] } ] }

        #assert woqlObject.json() == jsonObj
        assert woqlObjectChain.json() == jsonObj

    def test_star_method(self):
        woqlObject=WOQLQuery().limit(10).star()
        jsonObj={ 'limit': [ 10, { "triple": [
                      "v:Subject",
                      "v:Predicate",
                      "v:Object"
                    ] } ] }
        assert woqlObject.json() == jsonObj

    def test_select_method(self):
        woqlObject=WOQLQuery().select("V1", WOQLQuery().triple("a", "b", "c"));
        woqlObjectMultiple=WOQLQuery().select("V1", "V2", WOQLQuery().triple("a", "b", "c"));
        woqlObjectChain=WOQLQuery().select("V1").triple("a", "b", "c");
        woqlObjectChainMultiple=WOQLQuery().select("V1","V2").triple("a", "b", "c");

        jsonObj={ 'select': [ 'V1', { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] } ] }
        jsonObjMultiple={ 'select': [ 'V1', 'V2', { 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] } ] }

        assert woqlObject.json() == jsonObj
        assert woqlObjectChain.json() == jsonObj
        assert woqlObjectMultiple.json() == jsonObjMultiple
        assert woqlObjectChainMultiple.json() == jsonObjMultiple

    def test_eq_method(self):
        woqlObject=WOQLQuery().eq("a","b")
        jsonObj={ 'eq': [ { "@language": "en", "@value": "a" },
                        { "@language": "en", "@value": "b" } ] }
        assert woqlObject.json() == jsonObj

    def test_trim_method(self):
        woqlObject=WOQLQuery().trim("a","b")
        jsonObj={ 'trim': [ "a", "b" ] }
        assert woqlObject.json() == jsonObj

    def test_eval_method(self):
        woqlObject=WOQLQuery().eval("1+2","b")
        jsonObj={ 'eval': [ '1+2', 'b' ] }
        assert woqlObject.json() == jsonObj

    def test_minus_method(self):
        woqlObject=WOQLQuery().minus("2","1")
        jsonObj={ 'minus': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_plus_method(self):
        woqlObject=WOQLQuery().plus("2","1")
        jsonObj={ 'plus': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_times_method(self):
        woqlObject=WOQLQuery().times("2","1")
        jsonObj={ 'times': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_divide_method(self):
        woqlObject=WOQLQuery().divide("2","1")
        jsonObj={ 'divide': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_exp_method(self):
        woqlObject=WOQLQuery().exp("2","1")
        jsonObj={ 'exp': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_div_method(self):
        woqlObject=WOQLQuery().div("2","1")
        jsonObj={ 'div': [ '2', '1' ] }
        assert woqlObject.json() == jsonObj

    def test_get_method(self):
        woqlObject=WOQLQuery().get("Map", "Target")
        jsonObj={ 'get': [[], {}] }
        assert woqlObject.json() == jsonObj

    def test_WQOLas_method(self):
        woqlObject=WOQLQuery().WOQLas("Source", "Target")
        woqlObject2=WOQLQuery().WOQLas("Source", "Target").WOQLas("Source2", "Target2")
        jsonObj=[{ 'as': [ { '@value': 'Source' }, 'v:Target' ] }]
        jsonObj2 =[{ 'as': [ { '@value': 'Source' }, 'v:Target' ] },
                   { 'as': [ { '@value': 'Source2' }, 'v:Target2' ] }]

        assert woqlObject.json() == jsonObj
        assert woqlObject2.json() == jsonObj2

    def test_remote_method(self):
        woqlObject=WOQLQuery().remote({'url': "http://url"})
        jsonObj={ 'remote': [ { 'url': 'http://url' } ] }
        assert woqlObject.json() == jsonObj

    def test_idgen_method(self):
        woqlObject=WOQLQuery().idgen("doc:Station",["v:Start_ID"],"v:Start_Station_URL")
        jsonObj={ "idgen": [ 'doc:Station', { "list": ["v:Start_ID"] }, 'v:Start_Station_URL' ] }
        assert woqlObject.json() == jsonObj

    def test_typecast_method(self):
        woqlObject=WOQLQuery().typecast("v:Duration", "xsd:integer", "v:Duration_Cast")
        jsonObj={ "typecast": [ "v:Duration", "xsd:integer", "v:Duration_Cast" ] }
        assert woqlObject.json() == jsonObj


    def teat_list_method(self):
        woqlObject=WOQLQuery().list(["V1","V2"])
        jsonObj={ 'list': [ [ 'V1', 'V2' ] ] }
        assert woqlObject.json() == jsonObj


class TestTripleBuilder:

    def test_triple_method(self):
        woqlObject=WOQLQuery().triple("a", "b", "c")
        jsonObj={ 'triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] }
        assert woqlObject.json() == jsonObj

    def test_quad_method(self):
        woqlObject=WOQLQuery().quad("a", "b", "c", "d")
        jsonObj={ 'quad': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" }, "db:d" ] }
        assert woqlObject.json() == jsonObj

    def test_addClass_method(self):
        woqlObject=WOQLQuery().addClass("id")
        jsonObj={ 'add_quad': [ 'scm:id', 'rdf:type', 'owl:Class', 'db:schema' ] }
        assert woqlObject.json() == jsonObj

    def test_deleteClass_method(self):
        woqlObject=WOQLQuery().deleteClass("id")
        jsonObj= { 'and': [
          { 'delete_quad': [ 'scm:id', 'v:All', 'v:Al2', 'db:schema' ] },
          { 'opt': [ { 'delete_quad': [ 'v:Al3', 'v:Al4', 'scm:id', 'db:schema' ] } ] }
          ] }
        assert woqlObject.json() == jsonObj

    def test_sub_method(self):
        woqlObject=WOQLQuery().sub("ClassA","ClassB")
        jsonObj={ 'sub': [ "scm:ClassA", "scm:ClassB" ] }
        assert woqlObject.json() == jsonObj

    def test_isa_methos(self):
        woqlObject=WOQLQuery().isa("instance","Class")
        jsonObj={ 'isa': [ "scm:instance", "owl:Class" ] }
        assert woqlObject.json() == jsonObj

    def test_delete_method(self):
        woqlObject=WOQLQuery().delete({ 'triple': [ "doc:a",
                                                    "scm:b",
                                                    { "@language": "en", "@value": "c" } ] })
        jsonObj={ 'delete': [ { 'triple': [ "doc:a",
                                            "scm:b",
                                            { "@language": "en", "@value": "c" } ] } ] }
        assert woqlObject.json() == jsonObj

    def test_delete_triple_method(self):
        woqlObject=WOQLQuery().delete_triple("a", "b", "c")
        jsonObj={ 'delete_triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] }
        assert woqlObject.json() == jsonObj

    def test_delete_quad_method(self):
        woqlObject=WOQLQuery().delete_quad("a", "b", "c", "d")
        jsonObj={ 'delete_quad': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" }, "db:d" ] }
        assert woqlObject.json() == jsonObj

    def test_add_triple_method(self):
        woqlObject=WOQLQuery().add_triple("a", "b", "c")
        jsonObj={ 'add_triple': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" } ] }
        assert woqlObject.json() == jsonObj

    def test_add_quad_method(self):
        woqlObject=WOQLQuery().add_quad("a", "b", "c", "d")
        jsonObj={ 'add_quad': [ "doc:a", "scm:b", { "@language": "en", "@value": "c" }, "db:d" ] }
        assert woqlObject.json() == jsonObj

    def test_addProperty_methof(self):
        woqlObject=WOQLQuery().addProperty("some_property", "string")
        jsonObj={ 'and': [ { 'add_quad': [ 'scm:some_property', 'rdf:type', 'owl:DatatypeProperty', 'db:schema' ] }, { 'add_quad': [ 'scm:some_property', 'rdfs:range', 'xsd:string', 'db:schema' ] } ] }
        print(woqlObject.json())
        assert woqlObject.json() == jsonObj

    def test_deleteProperty_method(self):
        woqlObject=WOQLQuery().deleteProperty("some_property", "string")
        jsonObj={ 'and': [ { 'delete_quad': [ 'scm:some_property', 'v:All', 'v:Al2', 'xsd:string' ] }, { 'delete_quad': [ 'v:Al3', 'v:Al4', 'scm:some_property', 'xsd:string' ] } ] }
        assert woqlObject.json() == jsonObj


class TestTripleBuilderChainer:

    def test_node_method(self):
        woqlObject=WOQLQuery().node("some_node")
        jsonObj={}
        assert woqlObject.json() == jsonObj

    def test_graph_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").graph("db:schema")
        woqlObject2=WOQLQuery().node("doc:x", "add_quad").graph("db:mySchema").label("my label", "en")
        jsonObj={}
        jsonObj2={ 'add_quad': ['doc:x', 'rdfs:label', { '@value': 'my label', '@language': 'en' }, 'db:mySchema'] }

        assert woqlObject.json() == jsonObj
        assert woqlObject2.json() == jsonObj2

    def test_label_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").label("my label", "en")
        jsonObj={ 'add_quad': ['doc:x', 'rdfs:label', { '@value': 'my label', '@language': 'en' }, 'db:schema'] }
        assert woqlObject.json() == jsonObj

    def test_again_addClass_method(self):
        woqlObject=WOQLQuery().addClass("NewClass").description("A new class object.").entity()
        jsonObj={ "and": [{"add_quad": ['scm:NewClass', 'rdf:type', "owl:Class", 'db:schema']},
                      {"add_quad": ['scm:NewClass', 'rdfs:comment', { '@value': "A new class object.", '@language': 'en' }, 'db:schema']},
                      {"add_quad": ['scm:NewClass', 'rdfs:subClassOf', "tcs:Entity", 'db:schema']}
                ]}
        print(woqlObject.json())
        assert woqlObject.json() == jsonObj

    def test_comment_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").comment("my comment")
        jsonObj={ "comment": [
                {"@language": "en",
                  "@value": "my comment"},
                {}
                ] }
        assert woqlObject.json() == jsonObj

    def test_property_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").property("myprop", "value")
        jsonObj={ 'add_quad': ['doc:x',
                              'scm:myprop',
                              { '@value': 'value', '@language': 'en' },
                              'db:schema'] }
        assert woqlObject.json() == jsonObj

    def test_entity_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").entity()
        jsonObj={ 'add_quad': [ 'doc:x', 'rdfs:subClassOf', 'tcs:Entity', 'db:schema' ] }
        assert woqlObject.json() == jsonObj

    def test_parent_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").parent("Z")
        jsonObj={ 'add_quad': [ 'doc:x', 'rdfs:subClassOf', 'scm:Z', 'db:schema' ] }
        assert woqlObject.json() == jsonObj

    def test_abstract_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").abstract()
        jsonObj={ 'add_quad': [ 'doc:x', 'tcs:tag', 'tcs:abstract', 'db:schema' ] }
        assert woqlObject.json() == jsonObj

    def test_relationship_method(self):
        woqlObject=WOQLQuery().node("doc:x", "add_quad").relationship()
        jsonObj={ 'add_quad': [ 'doc:x', 'rdfs:subClassOf', 'tcs:Entity', 'db:schema' ] }
        assert woqlObject.json() == jsonObj

    def test_max_method(self):
        woqlObject=WOQLQuery().addProperty("P", "string").max(4)
        jsonObj={ "and": [ { "add_quad": ["scm:P",
                                            "rdf:type",
                                            "owl:DatatypeProperty",
                                            "db:schema"] },
                               { "add_quad": ["scm:P",
                                            "rdfs:range",
                                            "xsd:string",
                                            "db:schema"] },
                               { "add_quad": ["scm:P_max",
                                            "rdf:type",
                                            "owl:Restriction",
                                            "db:schema"] },
                               { "add_quad": [ "scm:P_max",
                                            "owl:onProperty",
                                            "scm:P",
                                            "db:schema"] },
                               { "add_quad": [ "scm:P_max",
                                            "owl:maxCardinality",
                                            { "@value": 4, "@type": "xsd:nonNegativeInteger" },
                                            "db:schema"] } ] }
        assert woqlObject.json() == jsonObj

    def test_min_method(self):
        woqlObject=WOQLQuery().addProperty("P", "string").min(2)
        jsonObj={ "and": [ { "add_quad": ["scm:P",
                                            "rdf:type",
                                            "owl:DatatypeProperty",
                                            "db:schema"] },
                                 { "add_quad": ["scm:P",
                                            "rdfs:range",
                                            "xsd:string",
                                            "db:schema"] },
                                 { "add_quad": ["scm:P_min",
                                            "rdf:type",
                                            "owl:Restriction",
                                            "db:schema"] },
                                 { "add_quad": [ "scm:P_min",
                                            "owl:onProperty",
                                            "scm:P",
                                            "db:schema"] },
                                 { "add_quad": [ "scm:P_min",
                                            "owl:minCardinality",
                                            { "@value": 2, "@type": "xsd:nonNegativeInteger" },
                                            "db:schema"] } ] }
        assert woqlObject.json() == jsonObj

    def test_cardinality_method(self):
        woqlObject=WOQLQuery().addProperty("P", "string").cardinality(3)
        jsonObj={ "and": [ { "add_quad": ["scm:P",
                                              "rdf:type",
                                              "owl:DatatypeProperty",
                                              "db:schema"] },
                                 { "add_quad": ["scm:P",
                                              "rdfs:range",
                                              "xsd:string",
                                              "db:schema"] },
                                 { "add_quad": ["scm:P_cardinality",
                                              "rdf:type",
                                              "owl:Restriction",
                                              "db:schema"] },
                                 { "add_quad": [ "scm:P_cardinality",
                                              "owl:onProperty",
                                              "scm:P",
                                              "db:schema"] },
                                 { "add_quad": [ "scm:P_cardinality",
                                              "owl:cardinality",
                                              { "@value": 3, "@type": "xsd:nonNegativeInteger" },
                                              "db:schema"] } ] }
        assert woqlObject.json() == jsonObj