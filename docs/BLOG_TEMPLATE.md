# Blog Entry Template

Use this template when creating new development blog entries.

## File Naming

- Location: `docs/blog/YYYY/MM-DD-title.rst`
- Example: `docs/blog/2026/01-15-diagnostic-engine.rst`

## Template

```rst
Entry Title
===========

:date: YYYY-MM-DD
:author: Your Name
:tags: milestone, technical-decision, challenge, feature

Context
-------

Why this entry exists and what prompted it.

- What problem are you solving?
- What milestone are you documenting?
- What decision needed to be made?

Decisions Made
--------------

Key decisions and their rationale.

Option Analysis
^^^^^^^^^^^^^^^

If multiple options were considered:

**Option 1: Description**

Pros:
- Pro 1
- Pro 2

Cons:
- Con 1
- Con 2

**Option 2: Description** (Selected)

Pros:
- Pro 1
- Pro 2

Cons:
- Con 1
- Con 2

Rationale: Why Option 2 was chosen.

Implementation Details
----------------------

Technical details about what was implemented.

Code Examples
^^^^^^^^^^^^^

.. code-block:: python

   def example_function() -> None:
       """Example of implemented code."""
       pass

Architecture Diagrams
^^^^^^^^^^^^^^^^^^^^^

Describe system architecture if relevant.

Challenges Encountered
----------------------

What problems did you face and how did you solve them?

Challenge 1: Description
^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Detailed description of the issue

**Solution**: How it was resolved

**Lesson**: What you learned

Challenge 2: Description
^^^^^^^^^^^^^^^^^^^^^^^^

...

Outcomes
--------

What were the results?

Metrics
^^^^^^^

- Lines of code added/changed
- Test coverage achieved
- Performance improvements
- Time taken

Quality Checks
^^^^^^^^^^^^^^

- [ ] Tests passing
- [ ] Coverage target met
- [ ] Linting clean
- [ ] Type checking passing
- [ ] Documentation updated

Next Steps
----------

What comes after this?

- Immediate next task
- Follow-up work needed
- Future enhancements

Lessons Learned
---------------

Key takeaways from this work.

What Worked Well
^^^^^^^^^^^^^^^^

Things that went smoothly.

What Could Be Improved
^^^^^^^^^^^^^^^^^^^^^^

Areas for future improvement.

Would Do Differently
^^^^^^^^^^^^^^^^^^^^

Hindsight insights.

References
----------

- Link to related issues
- Link to pull requests
- External documentation
- Related blog entries

---

*Additional notes or context.*
```

## Adding to Documentation

After creating the entry:

1. Add to `docs/blog.rst` toctree:
   ```rst
   .. toctree::
      :maxdepth: 1
      :reversed:

      blog/2026/MM-DD-title
   ```

2. Add to year archive `docs/blog-YYYY.rst`:
   ```rst
   .. toctree::
      :maxdepth: 1
      :reversed:

      blog/YYYY/MM-DD-title
   ```

3. Build and verify:
   ```bash
   cd docs
   pip install sphinx furo
   sphinx-build -b html . _build/html
   open _build/html/blog.html
   ```

## Common Tags

Use these tags for consistency:

- `milestone` - Major milestone achieved
- `technical-decision` - Important technical decision
- `challenge` - Problem solved or lesson learned
- `feature` - New feature implemented
- `refactor` - Code refactoring
- `performance` - Performance improvement
- `testing` - Testing strategy or coverage
- `infrastructure` - Build, CI/CD, tooling changes
- `documentation` - Documentation updates
- `security` - Security-related work

## Best Practices

- Write entries while the work is fresh
- Be honest about challenges and mistakes
- Include specific technical details
- Reference code and commits where relevant
- Keep entries focused on one topic
- Use consistent formatting
- Proofread before committing
