source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "bulma-clean-theme"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-include-cache"
end

# Optional: unterdrückt Faraday-Warnung bzgl. Retry-Middleware
gem "faraday-retry", "~> 2"

# Windows: vermeidet Polling für Dateiänderungen
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

# Windows: Timezone-Unterstützung
gem 'tzinfo', '~> 1.2' if Gem.win_platform?
gem 'tzinfo-data', platforms: [:windows, :jruby]

# sass-embedded (~> 1.75) verlangt google-protobuf < 4.32.
# Bundler installierte zuletzt 4.32.0, was den Resolver in eine Schleife schickte.
# Wir pinnen deshalb explizit auf 4.31.x.
gem 'google-protobuf', '~> 4.33.5'

