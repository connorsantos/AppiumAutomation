def test_check_all_box(home):
    accessAbilityView = home.nav_to_accessability()
    nodeQueryView = accessAbilityView.nav_to_access_node_query()
    curr_boxes = nodeQueryView.get_current_boxes_states()

    def assert_boxes(dict):
        for box in dict:
            match box:
                case "trash_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.TRASH_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.TRASH_BOX)
                        assert curr_boxes.get(box) is True
                case "laundry_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.LAUNDRY_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.LAUNDRY_BOX)
                        assert curr_boxes.get(box) is True
                case "conquer_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.CONQUER_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.CONQUER_BOX)
                        assert curr_boxes.get(box) is True
                case "nap_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.NAP_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.NAP_BOX)
                        assert curr_boxes.get(box) is True
                case "taxes_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
                        assert curr_boxes.get(box) is True
                case "irs_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.IRS_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.IRS_BOX)
                        assert curr_boxes.get(box) is True
                case "tea_box":
                    if(dict.get(box)):
                        nodeQueryView.check_box(nodeQueryView.TEA_BOX)
                        assert curr_boxes.get(box) is not True
                    else:
                        nodeQueryView.check_box(nodeQueryView.TEA_BOX)
                        assert curr_boxes.get(box) is True
    assert_boxes(curr_boxes)

def test_check_4_click_single_box(home):
    accessAbilityView = home.nav_to_accessability()
    nodeQueryView = accessAbilityView.nav_to_access_node_query()
    original_state = nodeQueryView.get_attr(nodeQueryView.TAXES_BOX, 'checked')
    nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
    assert original_state != nodeQueryView.get_attr(nodeQueryView.TAXES_BOX, 'checked')
    nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
    assert original_state == nodeQueryView.get_attr(nodeQueryView.TAXES_BOX, 'checked')
    nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
    assert original_state != nodeQueryView.get_attr(nodeQueryView.TAXES_BOX, 'checked')
    nodeQueryView.check_box(nodeQueryView.TAXES_BOX)
    assert original_state == nodeQueryView.get_attr(nodeQueryView.TAXES_BOX, 'checked')


