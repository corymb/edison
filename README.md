# Edison

Django-based web app to quickly search logfiles from the #python channel. 

# Usage

# Notes

  - Focused mostly on flexibility - it would be trivial to extend this to other channels or repurpose core functionality.
  - Overall not happy with the project I picked; there are better things to demonstrate my knowledge of software development. Lesson learned!
  - All code is PEP8 compliant.
  - Tests pass on each commit; I like this approach because it allows me to:
    - Benchmark (I have a script that checks running times) 
    - Quickly identify regressions (another script; I pass to git bisect)
  - I focused strongly on design by contract and adhering to SOLID - I'm not sure this is the best approach for this, but it illustrates my awareness at least.
  - In a production context, I would not take some of the shortcuts I did (I'm very uncomfortable with serving static assets how I have, for example)
  - In the real world, I would probably use tools better suited for this, but it's important that I illustrate my Python/Django knowledge.
  - I would also write some smoke-tests to check Django's views were doing what they should but I prefer splitting out logic to domain objects:
    - Classes should do one thing
    - I run tests every 3-30 seconds. At that frequency, I don't like involving the overhead of importing an entire framework (though this is borne out of coding in Ruby for years - it's possible Django isn't as terrible as Rails ins this regard!)
  - Hope this has been helpful!
