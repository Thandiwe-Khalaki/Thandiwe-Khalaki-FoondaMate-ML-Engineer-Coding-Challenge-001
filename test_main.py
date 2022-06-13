from main import check_mail
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [("Can I share your email", 'Student wants to know if can share'), ("I will share your email", 'Student wants to know if can share'),
     ("I shall share your email", 'Student wants to know if can share')],
)
def test_lower_case_present_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'share' and 'email"
    
@pytest.mark.parametrize(
    "test_input,expected",
    [("Can I Share your email", 'Student wants to know if can share'), ("I will share Your Email", 'Student wants to know if can share'),
     ("I Shall Share your Email", 'Student wants to know if can share')],
)
def test_mixed_case_present_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'share' and 'email"
    
@pytest.mark.parametrize(
    "test_input,expected",
    [("CAN I SHARE YOUR EMAIL", 'Student wants to know if can share'), ("I WILL SHARE YOUR EMAIL", 'Student wants to know if can share'),
     ("I SHALL SHARE YOUR EMAIL", 'Student wants to know if can share')],
)
def test_upper_case_present_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'share' and 'email"
@pytest.mark.parametrize(
    "test_input,expected",
    [("I've just shared your email", 'Student has shared'), ("I already shared the email", 'Student has shared'),
     ("I've shared your email", 'Student has shared')],
)
def test_lower_case_passed_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'shared' and 'email"
    
@pytest.mark.parametrize(
    "test_input,expected",
    [("I've just Shared your email", 'Student has shared'), ("I already shared the Email", 'Student has shared'),
     ("I've Shared your Email", 'Student has shared')],
)
def test_mixed_case_passed_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'shared' and 'email"
    
@pytest.mark.parametrize(
    "test_input,expected",
    [("I'VE JUST SHARED YOUR EMAIL", 'Student has shared'), ("I ALREADY SHARED THE EMAIL", 'Student has shared'),
     ("I'VE SHARED YOUR EMAIL", 'Student has shared')],
)
def test_upper_case_passed_tense(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'shared' and 'email"

@pytest.mark.parametrize(
    "test_input,expected",
    [("I've just shared your emails", 'Sentence has misspelt words or is invalid'), ("I already shareed the email", 'Sentence has misspelt words or is invalid'),
     ("I've shared your details", 'Sentence has misspelt words or is invalid')],
)
def test_failing_tests(test_input, expected):
    assert check_mail(test_input) == expected, "The sentence does not have the words 'share/shared' and 'email. Check spelling or the whole sentence"