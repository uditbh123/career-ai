# System Overview

## Vision

Career AI is an open-source AI-powered career platform designed to help job seekers throughout their career journey.

Instead of focusing only on resume generation, the platform provides a complete workflow that includes job discovery, resume optimization, cover letter generation, interview preparation, application tracking, company research, and career growth recommendations.

The platform is being built with a modular architecture so that support for additional countries, job portals, and AI providers can be added without changing the core application.

## Core Features

* User profile management
* AI-powered resume optimization
* AI-generated cover letters
* Job search from multiple sources
* Job recommendation and ranking
* Company insights
* Application tracking
* Interview preparation
* Skill gap analysis

## High-Level Architecture

User

↓

Frontend (Next.js)

↓

REST API

↓

Backend (FastAPI)

↓

Business Services

↓

Database (PostgreSQL)

↓

External Services

* AI Providers
* Job Boards
* Company Websites

## Design Principles

* Modular architecture
* Separation of concerns
* Scalable components
* API-first development
* Testability
* Maintainability
