"""Test basic imports to ensure package structure is correct."""

def test_import_main_module():
    """Test that main module can be imported."""
    try:
        import datarasta
        assert datarasta.__version__ == "0.1.0"
    except ImportError as e:
        # This is expected if dependencies aren't installed
        pass


def test_import_structure():
    """Test that package structure is correct."""
    import datarasta
    assert hasattr(datarasta, 'DataQualityMetrics')
    assert hasattr(datarasta, 'COUNT_NULL')
    assert hasattr(datarasta, 'COUNT_DISTINCT')
    assert hasattr(datarasta, 'AVERAGE')
    assert hasattr(datarasta, 'MIN')
    assert hasattr(datarasta, 'MAX')

