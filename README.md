# Docker Image Hardening Lab

## Objective
Transform a vulnerable Docker image into a hardened production-ready container image.

## Security Issues in Vulnerable Image
- Running container as root
- Embedded secrets in image
- Large attack surface
- Unnecessary packages installed
- No image optimization

## Hardening Techniques Implemented
- Multi-stage builds
- Alpine-based image
- Non-root container execution
- Reduced package footprint
- Environment variable separation
- Optimized dependency installation

## Results

### Image Size Comparison
| Image | Size |
|---|---|
| Vulnerable | 842MB |
| Multistage | 194MB |
| Hardened Alpine | 91MB |

Reduced image size from 842MB to 91MB using Alpine and multi-stage builds while enforcing non-root execution and removing embedded secrets.

### Security Scanning
- Trivy vulnerability scans performed
- Docker Bench Security checks executed
- CIS Docker Benchmark reviewed

## Project Structure

```text
app/
hardened/
multistage/
vulnerable/
reports/
screenshots/
