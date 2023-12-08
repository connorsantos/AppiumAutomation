def test_uncheck_box(home):
    accessAbilityView = home.nav_to_accessability()

    nodeQueryView = accessAbilityView.nav_to_access_node_query()
    nodeQueryView.check_trash_box()
    trash_box = nodeQueryView.get_trash_box_item()
    print(trash_box)
    assert trash_box is True


